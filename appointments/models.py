from django.db import models
from django.contrib.auth.models import User


class Appointment(models.Model):

    STATUS_CHOICES = (

        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),

    )

    patient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='patient_appointments'
    )

    doctor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='doctor_appointments'
    )

    appointment_date = models.DateField()

    appointment_time = models.TimeField()

    age = models.IntegerField()

    phone = models.CharField(max_length=15)

    gender = models.CharField(max_length=10)

    message = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return f"{self.patient.username} -> {self.doctor.username}"