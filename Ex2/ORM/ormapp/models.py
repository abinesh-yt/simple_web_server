from django.db import models
from django.contrib import admin

# Example: Student Registration System
class Student(models.Model):
    first_name = models.CharField(max_length=50)   # Text field
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)         # Email field
    password = models.CharField(max_length=100)    # For demo, normally use Django's auth User model
    age = models.PositiveIntegerField()            # Number field
    phone = models.CharField(max_length=15, blank=True, null=True)
                # Date field
    admission_date = models.DateTimeField(auto_now_add=True)  # DateTime field

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

   
class StudentAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name","email","password","age","phone","admission_date")
