from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
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
