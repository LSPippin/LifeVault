from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def landing_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'core/landing.html')


@login_required
def dashboard_view(request):
    context = {
        'user': request.user,
        'categories': [
            {'name': 'Health', 'icon': '🏥', 'slug': 'health', 'count': 0},
            {'name': 'Insurance', 'icon': '🛡️', 'slug': 'insurance', 'count': 0},
            {'name': 'Home & Maintenance', 'icon': '🏠', 'slug': 'home', 'count': 0},
            {'name': 'Vehicles', 'icon': '🚗', 'slug': 'vehicles', 'count': 0},
            {'name': 'Financial & Tax', 'icon': '💰', 'slug': 'financial', 'count': 0},
            {'name': 'Pets', 'icon': '🐾', 'slug': 'pets', 'count': 0},
            {'name': 'Vendors & Services', 'icon': '🔧', 'slug': 'vendors', 'count': 0},
        ],
    }
    return render(request, 'core/dashboard.html', context)
