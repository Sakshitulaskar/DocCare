
from django.shortcuts import render
from doctors.models import Doctor


def home(request):

    return render(request, 'home.html')


def about(request):

    return render(request, 'about.html')


def services(request):

    return render(request, 'services.html')


def contact(request):

    return render(request, 'contact.html')

from django.shortcuts import render


def symptom_checker(request):

    disease = None
    doctor = None
    recommended_doctors = None

    if request.method == "POST":

        symptoms = request.POST.get('symptoms').lower()

        # AI Logic

        if 'fever' in symptoms and 'cough' in symptoms:

            disease = "Flu or Viral Infection"
            doctor = "General Physician"

        elif 'chest pain' in symptoms:

            disease = "Heart Related Problem"
            doctor = "Cardiologist"

        elif 'tooth pain' in symptoms:

            disease = "Dental Infection"
            doctor = "Dentist"

        elif 'skin' in symptoms or 'rash' in symptoms:

            disease = "Skin Allergy"
            doctor = "Dermatologist"

        elif 'eye' in symptoms:

            disease = "Eye Infection"
            doctor = "Eye Specialist"

        else:

            disease = "Symptoms not recognized"
            doctor = "Consult General Physician"

        # Recommended Doctors

        if doctor:

            recommended_doctors = Doctor.objects.filter(
                specialization__icontains=doctor
            )

    return render(
        request,
        'symptom_checker.html',
        {
            'disease': disease,
            'doctor': doctor,
            'recommended_doctors': recommended_doctors
        }
    )