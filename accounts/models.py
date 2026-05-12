

from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):

    ROLE_CHOICES = (

        ('doctor', 'Doctor'),
        ('patient', 'Patient'),

    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    # Doctor Details

    specialization = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    experience = models.IntegerField(
        blank=True,
        null=True
    )

    qualification = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    image = models.ImageField(
        upload_to='doctor_images/',
        blank=True,
        null=True
    )

    def __str__(self):

        return self.user.username