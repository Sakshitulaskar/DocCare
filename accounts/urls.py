"""
URL configuration for doccare project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [

    path('register/', views.register_view, name='register'),

    path('login/', views.login_view, name='login'),

    path('logout/', views.logout_view, name='logout'),

    path('patient-dashboard/', views.patient_dashboard, name='patient_dashboard'),

    path('doctor-dashboard/', views.doctor_dashboard, name='doctor_dashboard'),

    path('approve-appointment/<int:appointment_id>/',views.approve_appointment,name='approve_appointment'),

    path('reject-appointment/<int:appointment_id>/', views.reject_appointment, name='reject_appointment'),

    path(
    'cancel-appointment/<int:appointment_id>/',
    views.cancel_appointment,
    name='cancel_appointment'
),
]