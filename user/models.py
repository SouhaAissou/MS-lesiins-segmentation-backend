from django.db import models
from django.contrib.auth import models as auth_models

# Create your models here.

class UserManager(auth_models.BaseUserManager):
    
    def create_user(self, last_name:str, first_name:str, email:str, role:str, phone_number:str, password:str = None, is_active=True, is_staff=False, is_superuser=False) -> "User":
        if not email:
            raise ValueError("User must have an email address")
        if not first_name:
            raise ValueError("User must have a first name")
        if not last_name:
            raise ValueError("User must have a last name")
        
        user = self.model(email=self.normalize_email(email), )
        user.first_name = first_name
        user.last_name = last_name
        user.role = role
        user.phone_number = phone_number
        user.set_password(password)
        user.is_active = is_active
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()
        
        return user
    
    def create_superuser(self, last_name:str, first_name:str, email:str, password:str = None)-> "User":
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            role="admin",  # Default role for superuser
            phone_number="123456789",  # Default phone number for superuser
            password=password,
            is_staff=True,
            is_superuser=True
        )
        return user
        

class User(auth_models.AbstractUser):
    first_name = models.CharField(verbose_name="First name", max_length=255)
    last_name = models.CharField(verbose_name="Last name", max_length=255)
    email = models.EmailField(verbose_name="Email", max_length=255, unique=True)
    role = models.CharField(verbose_name="Role", max_length=255)
    phone_number = models.CharField(max_length=255, verbose_name="Phone Number")
    is_active = models.BooleanField(verbose_name="Is Active", default=True)
    password = models.CharField( max_length=255)
    username = None
    
    objects = UserManager()
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]
    
    def __str__(self):
        return self.email or ''
    

    

