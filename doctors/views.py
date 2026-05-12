from django.shortcuts import render, redirect

from django.contrib.auth.models import User

from accounts.models import Profile

from django.contrib.auth.decorators import login_required

from .models import Doctor



def doctor_list(request):

    query = request.GET.get('q')

    doctors = Doctor.objects.all()


    if query:

        doctors = doctors.filter(
            specialization__icontains=query
        ) | doctors.filter(
            user__username__icontains=query
        )


    return render(
        request,
        'doctor_list.html',
        {
            'doctors': doctors
        }
    )



@login_required
def create_doctor_profile(request):

    if request.method == 'POST':

        specialization = request.POST['specialization']

        qualification = request.POST['qualification']

        experience = request.POST['experience']

        hospital = request.POST['hospital']

        fees = request.POST['fees']

        image = request.FILES['image']


        Doctor.objects.create(

            user=request.user,

            specialization=specialization,

            qualification=qualification,

            experience=experience,

            hospital=hospital,

            fees=fees,

            image=image

        )

        return redirect('doctor_list')


    return render(
        request,
        'create_doctor_profile.html'
    )




def doctor_detail(request, id):

    doctor = Doctor.objects.get(id=id)

    return render(
        request,
        'doctor_detail.html',
        {
            'doctor': doctor
        }
    )