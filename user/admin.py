from django.contrib import admin
from . import models

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "role", "phone_number", "is_staff", "is_superuser","is_active")
    


admin.site.register(models.User, UserAdmin)