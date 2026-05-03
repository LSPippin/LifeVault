# core/views.py
# Handles the main views for LifeVault including the landing page,
# dashboard, and global search functionality.
# The dashboard aggregates data from multiple models to give users
# a complete overview of their vault on login.

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.utils import timezone
from vault.models import Category, Record
from pets.models import Pet
from vehicles.models import Vehicle


# Landing page — redirects authenticated users directly to their dashboard
def landing_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'core/landing.html')


# Dashboard view — requires login
# Pulls categories, recent records, alerts, and counts from the database
# All queries are filtered by request.user to ensure data privacy
@login_required
def dashboard_view(request):
    # Fetch all categories belonging to the logged-in user
    categories = Category.objects.filter(user=request.user)

    # Fetch the 5 most recently created records for the activity feed
    recent_records = Record.objects.filter(
        user=request.user
    ).order_by('-created_at')[:5]

    # Get today's date for comparing against reminder dates
    today = timezone.now().date()

    # Fetch records where reminder date is today or in the past (due or overdue)
    alerts = Record.objects.filter(
        user=request.user,
        reminder_date__isnull=False,
        reminder_date__lte=today
    ).order_by('reminder_date')

    # Count pets and vehicles for the dashboard category tiles
    pet_count = Pet.objects.filter(user=request.user).count()
    vehicle_count = Vehicle.objects.filter(user=request.user).count()

    context = {
        'categories': categories,
        'recent_records': recent_records,
        'alerts': alerts,
        'today': today,
        'pet_count': pet_count,
        'vehicle_count': vehicle_count,
    }
    return render(request, 'core/dashboard.html', context)


# Global search view — searches across records, pets, and vehicles
# Uses Django Q objects to search multiple fields with OR logic
# icontains performs a case-insensitive search
@login_required
def search_view(request):
    # Get the search query from the URL parameter e.g. /search/?q=wicket
    query = request.GET.get('q', '')
    records = []
    pets = []
    vehicles = []

    if query:
        # Search generic records by title and notes
        records = Record.objects.filter(
            user=request.user
        ).filter(
            Q(title__icontains=query) | Q(notes__icontains=query)
        ).order_by('-created_at')

        # Search pet profiles by name, breed, species, and notes
        pets = Pet.objects.filter(
            user=request.user
        ).filter(
            Q(name__icontains=query) | Q(breed__icontains=query) |
            Q(species__icontains=query) | Q(notes__icontains=query)
        )

        # Search vehicles by make, model, VIN, and notes
        vehicles = Vehicle.objects.filter(
            user=request.user
        ).filter(
            Q(make__icontains=query) | Q(model__icontains=query) |
            Q(vin__icontains=query) | Q(notes__icontains=query)
        )

    context = {
        'query': query,
        'results': records,
        'pet_results': pets,
        'vehicle_results': vehicles,
    }
    return render(request, 'core/search.html', context)
