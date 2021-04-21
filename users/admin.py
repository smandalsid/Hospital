from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Patient, Doctor
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['email', 'username','is_staff','is_patient', 'is_doctor']

admin.site.register(User,CustomUserAdmin)
admin.site.register(Patient)
admin.site.register(Doctor)
