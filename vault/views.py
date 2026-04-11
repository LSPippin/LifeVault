from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Record
from .forms import RecordForm


@login_required
def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug, user=request.user)
    records = Record.objects.filter(
        category=category
    ).order_by('-created_at')

    context = {
        'category': category,
        'records': records,
    }
    return render(request, 'vault/category_detail.html', context)


@login_required
def record_create(request, slug):
    category = get_object_or_404(Category, slug=slug, user=request.user)

    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.user = request.user
            record.category = category
            record.save()
            return redirect('category_detail', slug=slug)
    else:
        form = RecordForm()

    context = {
        'form': form,
        'category': category,
    }
    return render(request, 'vault/record_create.html', context)
