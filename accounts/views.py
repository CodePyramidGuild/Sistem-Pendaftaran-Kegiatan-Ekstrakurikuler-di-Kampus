from django.urls import reverse
from django.shortcuts import render, redirect

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.middleware.csrf import CsrfViewMiddleware  
from .forms import CustomUserCreationForm

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun berhasil dibuat. Silakan masuk.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})



def profile_view(request):
    return render(request, 'accounts/profile.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Anda berhasil masuk.')
                return redirect(reverse('extracurricular:halaman_utama'))
            else:
                messages.error(request, 'Username atau password salah.')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'Anda telah berhasil keluar.')
    return redirect('login')
