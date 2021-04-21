"""hospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from users.views import PatientSignUpView, DoctorSignUpView

urlpatterns = [
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('users/signup/patientsignup/', PatientSignUpView.as_view(template_name='patient_signup.html'), name='patient_signup'),
    path('users/signup/doctorsignup/', DoctorSignUpView.as_view(template_name='doctor_signup.html'), name='doctor_signup'),
    path('', TemplateView.as_view(template_name='home.html'),name='home'),
    path('admin/', admin.site.urls),
]
