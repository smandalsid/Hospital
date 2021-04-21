from django.db import models
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField

SEX_CHOICES=(
    (1,"Male"),
    (2, "Female"),
)

DEGREE_CHOICES=(
    (1, "M.B.B.S"),
    (2, "M.A."),
)

class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    sex = MultiSelectField(choices=SEX_CHOICES, max_choices=1)

    def __str__(self):
        return self.user.username

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    degree = MultiSelectField(choices=DEGREE_CHOICES)


    def __str__(self):
        return self.user.username