from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Vehicle, VehicleMaintenance, OilChange
from .forms import VehicleForm, VehicleMaintenanceForm, OilChangeForm


@login_required
def vehicle_list(request):
    vehicles = Vehicle.objects.filter(user=request.user)
    return render(request, 'vehicles/vehicle_list.html', {'vehicles': vehicles})


@login_required
def vehicle_create(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            vehicle = form.save(commit=False)
            vehicle.user = request.user
            vehicle.save()
            return redirect('vehicle_detail', pk=vehicle.pk)
    else:
        form = VehicleForm()
    return render(request, 'vehicles/vehicle_form.html', {'form': form, 'title': 'Add Vehicle'})


@login_required
def vehicle_detail(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk, user=request.user)
    maintenance = VehicleMaintenance.objects.filter(vehicle=vehicle).order_by('-date')
    oil_changes = OilChange.objects.filter(vehicle=vehicle).order_by('-date')
    context = {
        'vehicle': vehicle,
        'maintenance': maintenance,
        'oil_changes': oil_changes,
    }
    return render(request, 'vehicles/vehicle_detail.html', context)


@login_required
def vehicle_edit(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk, user=request.user)
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('vehicle_detail', pk=vehicle.pk)
    else:
        form = VehicleForm(instance=vehicle)
    return render(request, 'vehicles/vehicle_form.html', {'form': form, 'title': 'Edit Vehicle'})


@login_required
def vehicle_delete(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk, user=request.user)
    if request.method == 'POST':
        vehicle.delete()
        return redirect('vehicle_list')
    return render(request, 'vehicles/vehicle_confirm_delete.html', {'vehicle': vehicle})


@login_required
def maintenance_create(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk, user=request.user)
    if request.method == 'POST':
        form = VehicleMaintenanceForm(request.POST, request.FILES)
        if form.is_valid():
            record = form.save(commit=False)
            record.vehicle = vehicle
            record.save()
            return redirect('vehicle_detail', pk=vehicle.pk)
    else:
        form = VehicleMaintenanceForm()
    return render(request, 'vehicles/sub_form.html', {
        'form': form,
        'title': f'Add Maintenance for {vehicle.year} {vehicle.make} {vehicle.model}',
        'vehicle': vehicle
    })


@login_required
def oilchange_create(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk, user=request.user)
    if request.method == 'POST':
        form = OilChangeForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.vehicle = vehicle
            record.save()
            return redirect('vehicle_detail', pk=vehicle.pk)
    else:
        form = OilChangeForm()
    return render(request, 'vehicles/sub_form.html', {
        'form': form,
        'title': f'Add Oil Change for {vehicle.year} {vehicle.make} {vehicle.model}',
        'vehicle': vehicle
    })
