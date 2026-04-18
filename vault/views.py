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
        form = RecordForm(request.POST, request.FILES)
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


@login_required
def record_edit(request, pk):
    record = get_object_or_404(Record, pk=pk, user=request.user)

    if request.method == 'POST':
        form = RecordForm(request.POST, request.FILES, instance=record)
        if form.is_valid():
            form.save()
            return redirect('category_detail', slug=record.category.slug)
    else:
        form = RecordForm(instance=record)

    context = {
        'form': form,
        'record': record,
        'category': record.category,
    }
    return render(request, 'vault/record_edit.html', context)


@login_required
def record_delete(request, pk):
    record = get_object_or_404(Record, pk=pk, user=request.user)

    if request.method == 'POST':
        slug = record.category.slug
        record.delete()
        return redirect('category_detail', slug=slug)

    context = {
        'record': record,
        'category': record.category,
    }
    return render(request, 'vault/record_delete.html', context)
