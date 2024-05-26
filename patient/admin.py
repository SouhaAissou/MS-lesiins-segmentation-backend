from django.contrib import admin
from .models import Patient, Diagnostic, Segmentation

# Register your models here.

admin.site.register(Patient)
admin.site.register(Diagnostic)
admin.site.register(Segmentation)