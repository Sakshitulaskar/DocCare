
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Profile
from appointments.models import Appointment





    


# Register

def register_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        role = request.POST.get("role")

        if User.objects.filter(username=username).exists():

            messages.error(request, "Username already exists")
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        user.save()

        # profile create
        Profile.objects.create(
            user=user,
            role=role
        )

        messages.success(request, "Account Created Successfully")

        return redirect('login')

    return render(request, 'register.html')


# Login
def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            # Admin Login
            if user.is_superuser:

                return redirect('/admin/')

            profile, created = Profile.objects.get_or_create(

                user=user,

                defaults={
                    'role': 'patient'
                }

            )

            # Doctor Login
            if profile.role == "doctor":

                return redirect('doctor_dashboard')

            # Patient Login
            elif profile.role == "patient":

                return redirect('patient_dashboard')

        else:

            messages.error(request, "Invalid Username or Password")

    return render(request, 'login.html')
     


# Logout

def logout_view(request):

    logout(request)

    return redirect('login')

def patient_dashboard(request):

    appointments = Appointment.objects.filter(
        patient=request.user
    ).order_by('-created_at')

    return render(request, 'patient_dashboard.html', {
        'appointments': appointments
    })


def doctor_dashboard(request):

    appointments = Appointment.objects.filter(
        doctor=request.user
    ).order_by('-created_at')

    return render(request, 'doctor_dashboard.html', {
        'appointments': appointments
    })

def approve_appointment(request, appointment_id):

    appointment = Appointment.objects.get(id=appointment_id)

    appointment.status = "Approved"

    appointment.save()

    return redirect('doctor_dashboard')


def reject_appointment(request, appointment_id):

    appointment = Appointment.objects.get(id=appointment_id)

    appointment.status = "Rejected"

    appointment.save()

    return redirect('doctor_dashboard')

def cancel_appointment(request, appointment_id):

    appointment = Appointment.objects.get(id=appointment_id)

    appointment.delete()

    return redirect('patient_dashboard')