from django.contrib import admin

# Register your models here.
from .models import Student , StudentAdmin
admin.site.register(Student,StudentAdmin)