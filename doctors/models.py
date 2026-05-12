from django.db import models
from django.contrib.auth.models import User


class Doctor(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    specialization = models.CharField(
        max_length=100
    )

    qualification = models.CharField(
        max_length=200
    )

    experience = models.IntegerField()

    hospital = models.CharField(
        max_length=200
    )

    fees = models.IntegerField()

    image = models.ImageField(
        upload_to='doctor_images/'
    )

    def __str__(self):

        return self.user.username