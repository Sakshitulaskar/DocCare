from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Appointment
from appointments.models import Appointment

@login_required(login_url='login')
def book_appointment(request, doctor_id):

    doctor = User.objects.get(id=doctor_id)

    if request.method == "POST":

        appointment_date = request.POST.get("date")
        appointment_time = request.POST.get("time")

        age = request.POST.get("age")
        phone = request.POST.get("phone")
        gender = request.POST.get("gender")

        message = request.POST.get("message")

        Appointment.objects.create(

            patient=request.user,
            doctor=doctor,

            appointment_date=appointment_date,
            appointment_time=appointment_time,

            age=age,
            phone=phone,
            gender=gender,

            message=message

        )

        messages.success(request, "Appointment Booked Successfully")

        return redirect('patient_dashboard')

    return render(request, 'book_appointment.html', {
        'doctor': doctor
    })