from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Pet, PetAppointment, PetMedication, PetVaccine
from .forms import PetForm, PetAppointmentForm, PetMedicationForm, PetVaccineForm


@login_required
def pet_list(request):
    pets = Pet.objects.filter(user=request.user)
    return render(request, 'pets/pet_list.html', {'pets': pets})


@login_required
def pet_create(request):
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.user = request.user
            pet.save()
            return redirect('pet_detail', pk=pet.pk)
    else:
        form = PetForm()
    return render(request, 'pets/pet_form.html', {'form': form, 'title': 'Add Pet'})


@login_required
def pet_detail(request, pk):
    pet = get_object_or_404(Pet, pk=pk, user=request.user)
    appointments = PetAppointment.objects.filter(pet=pet).order_by('date')
    medications = PetMedication.objects.filter(pet=pet)
    vaccines = PetVaccine.objects.filter(pet=pet)
    context = {
        'pet': pet,
        'appointments': appointments,
        'medications': medications,
        'vaccines': vaccines,
    }
    return render(request, 'pets/pet_detail.html', context)


@login_required
def pet_edit(request, pk):
    pet = get_object_or_404(Pet, pk=pk, user=request.user)
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet_detail', pk=pet.pk)
    else:
        form = PetForm(instance=pet)
    return render(request, 'pets/pet_form.html', {'form': form, 'title': 'Edit Pet'})


@login_required
def pet_delete(request, pk):
    pet = get_object_or_404(Pet, pk=pk, user=request.user)
    if request.method == 'POST':
        pet.delete()
        return redirect('pet_list')
    return render(request, 'pets/pet_confirm_delete.html', {'pet': pet})


@login_required
def appointment_create(request, pk):
    pet = get_object_or_404(Pet, pk=pk, user=request.user)
    if request.method == 'POST':
        form = PetAppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.pet = pet
            appointment.save()
            return redirect('pet_detail', pk=pet.pk)
    else:
        form = PetAppointmentForm()
    return render(request, 'pets/sub_form.html', {
        'form': form,
        'title': f'Add Appointment for {pet.name}',
        'pet': pet
    })


@login_required
def medication_create(request, pk):
    pet = get_object_or_404(Pet, pk=pk, user=request.user)
    if request.method == 'POST':
        form = PetMedicationForm(request.POST)
        if form.is_valid():
            medication = form.save(commit=False)
            medication.pet = pet
            medication.save()
            return redirect('pet_detail', pk=pet.pk)
    else:
        form = PetMedicationForm()
    return render(request, 'pets/sub_form.html', {
        'form': form,
        'title': f'Add Medication for {pet.name}',
        'pet': pet
    })


@login_required
def vaccine_create(request, pk):
    pet = get_object_or_404(Pet, pk=pk, user=request.user)
    if request.method == 'POST':
        form = PetVaccineForm(request.POST, request.FILES)
        if form.is_valid():
            vaccine = form.save(commit=False)
            vaccine.pet = pet
            vaccine.save()
            return redirect('pet_detail', pk=pet.pk)
    else:
        form = PetVaccineForm()
    return render(request, 'pets/sub_form.html', {
        'form': form,
        'title': f'Add Vaccine for {pet.name}',
        'pet': pet
    })
