from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    DOCTOR = "DOCTOR"
    PATIENT = "PATIENT"
    USER_TYPE = (
        (DOCTOR, "doctor"),
        (PATIENT, "Patient") 
    )
    user_type = models.CharField(choices = USER_TYPE, null=True, blank=True, max_length=15)