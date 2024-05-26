from django.db import models

# from user.models import User
from django.conf import settings



class Patient(models.Model):
    first_name = models.CharField(verbose_name="First name", max_length=255)
    last_name = models.CharField(verbose_name="Last name", max_length=255)
    phone_number = models.CharField(max_length=255, verbose_name="Phone Number")
    email = models.EmailField(verbose_name="Email", max_length=255, unique=True)
    date_of_birth = models.CharField(max_length=255, verbose_name="Date of birth", default="")
    
    
class Diagnostic(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name="Patient")
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Doctor")
    date_diagnostic = models.CharField(max_length=255, verbose_name="Date of diagnostic")
    date_visit = models.CharField(max_length=255, verbose_name="Date of visit")
    diagnostic = models.TextField(verbose_name="Diagnostic")
    # treatment = models.CharField(max_length=255)
    # prescription = models.CharField(max_length=255)
    note = models.CharField(max_length=255, verbose_name="Note")
    
    
class Segmentation(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name="Patient")
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Doctor")
    date_segmentation = models.CharField(max_length=255, verbose_name="Date of segmentation")
    original_image = models.ImageField(verbose_name="Original Image")
    segmented_image = models.ImageField(verbose_name="Segmented Image")
    note = models.CharField(max_length=255, verbose_name="Note")
    
    
