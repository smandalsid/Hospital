from django.shortcuts import redirect, render
from django.contrib.auth import login, logout,authenticate
from django.views.generic import CreateView
from .forms import PatientSignUpForm, DoctorSignUpForm
from .models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.urls import reverse_lazy

class PatientSignUpView(CreateView):
    model = User
    form_class = PatientSignUpForm
    success_url = reverse_lazy('login')
    template_name = '../templates/patient_signup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

def register(request):
    return render(request, 'signup.html')


class DoctorSignUpView(CreateView):
    model = User
    form_class = DoctorSignUpForm
    success_url = reverse_lazy('login')
    template_name = '../templates/doctor_signup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('/')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, '../templates/registration/login.html',
    context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('/')