from django.urls import path
from .views import PatientSignUpView, DoctorSignUpView, register, login_request, logout_view

urlpatterns=[
    path('signup/', register, name='signup'),
    path('signup/patient_signup/', PatientSignUpView.as_view(), name='patient_sigup'),
    path('signup/doctor_signup/', DoctorSignUpView.as_view(), name='doctor_signup'),
    path('logout/',logout_view, name='logout'),
]