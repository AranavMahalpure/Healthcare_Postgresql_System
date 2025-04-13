from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User, Patient, Doctor, PatientDoctorMapping
from .forms import (
    UserRegistrationForm, UserLoginForm,
    PatientForm, DoctorForm, PatientDoctorMappingForm
)

# Authentication Views
def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('patient-list')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('patient-list')
        else:
            messages.error(request, 'Invalid email or password')
    else:
        form = UserLoginForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')

# Patient Views
@login_required
def patient_list(request):
    patients = Patient.objects.filter(created_by=request.user)
    return render(request, 'patients/list.html', {'patients': patients})

@login_required
def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk, created_by=request.user)
    return render(request, 'patients/detail.html', {'patient': patient})

@login_required
def patient_create(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.created_by = request.user
            patient.save()
            messages.success(request, 'Patient created successfully!')
            return redirect('patient-list')
    else:
        form = PatientForm()
    return render(request, 'patients/form.html', {'form': form, 'title': 'Create Patient'})

@login_required
def patient_update(request, pk):
    patient = get_object_or_404(Patient, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, 'Patient updated successfully!')
            return redirect('patient-detail', pk=patient.pk)
    else:
        form = PatientForm(instance=patient)
    return render(request, 'patients/form.html', {'form': form, 'title': 'Update Patient'})

@login_required
def patient_delete(request, pk):
    patient = get_object_or_404(Patient, pk=pk, created_by=request.user)
    if request.method == 'POST':
        patient.delete()
        messages.success(request, 'Patient deleted successfully!')
        return redirect('patient-list')
    return render(request, 'patients/confirm_delete.html', {'patient': patient})

# Doctor Views
@login_required
def doctor_list(request):
    doctors = Doctor.objects.filter(created_by=request.user)
    return render(request, 'doctors/list.html', {'doctors': doctors})

@login_required
def doctor_detail(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk, created_by=request.user)
    return render(request, 'doctors/detail.html', {'doctor': doctor})

@login_required
def doctor_create(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            doctor = form.save(commit=False)
            doctor.created_by = request.user
            doctor.save()
            messages.success(request, 'Doctor created successfully!')
            return redirect('doctor-list')
    else:
        form = DoctorForm()
    return render(request, 'doctors/form.html', {'form': form, 'title': 'Create Doctor'})

@login_required
def doctor_update(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Doctor updated successfully!')
            return redirect('doctor-detail', pk=doctor.pk)
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'doctors/form.html', {'form': form, 'title': 'Update Doctor'})

@login_required
def doctor_delete(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk, created_by=request.user)
    if request.method == 'POST':
        doctor.delete()
        messages.success(request, 'Doctor deleted successfully!')
        return redirect('doctor-list')
    return render(request, 'doctors/confirm_delete.html', {'doctor': doctor})

# Mapping Views
@login_required
def mapping_list(request):
    mappings = PatientDoctorMapping.objects.filter(created_by=request.user)
    return render(request, 'mappings/list.html', {'mappings': mappings})

@login_required
def mapping_create(request):
    if request.method == 'POST':
        form = PatientDoctorMappingForm(request.user, request.POST)
        if form.is_valid():
            mapping = form.save(commit=False)
            mapping.created_by = request.user
            mapping.save()
            messages.success(request, 'Doctor assigned to patient successfully!')
            return redirect('mapping-list')
    else:
        form = PatientDoctorMappingForm(request.user)
    return render(request, 'mappings/form.html', {'form': form, 'title': 'Assign Doctor to Patient'})

@login_required
def mapping_delete(request, pk):
    mapping = get_object_or_404(PatientDoctorMapping, pk=pk, created_by=request.user)
    if request.method == 'POST':
        mapping.delete()
        messages.success(request, 'Mapping deleted successfully!')
        return redirect('mapping-list')
    return render(request, 'mappings/confirm_delete.html', {'mapping': mapping})