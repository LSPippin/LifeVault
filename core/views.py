from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from vault.models import Category, Record


def landing_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'core/landing.html')


@login_required
def dashboard_view(request):
    categories = Category.objects.filter(user=request.user)
    recent_records = Record.objects.filter(
        user=request.user
    ).order_by('-created_at')[:5]

    context = {
        'categories': categories,
        'recent_records': recent_records,
    }
    return render(request, 'core/dashboard.html', context)


@login_required
def search_view(request):
    query = request.GET.get('q', '')
    results = []

    if query:
        results = Record.objects.filter(
            user=request.user
        ).filter(
            Q(title__icontains=query) | Q(notes__icontains=query)
        ).order_by('-created_at')

    context = {
        'query': query,
        'results': results,
    }
    return render(request, 'core/search.html', context)
