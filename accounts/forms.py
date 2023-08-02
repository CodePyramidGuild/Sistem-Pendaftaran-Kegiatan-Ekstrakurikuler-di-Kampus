from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    alamat = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'border rounded w-full p-2'})
    )
    nomor_telepon = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'border rounded w-full p-2'})
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'alamat', 'nomor_telepon', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'border rounded w-full p-2'}),
            'password1': forms.PasswordInput(attrs={'class': 'border rounded w-full p-2'}),
            'password2': forms.PasswordInput(attrs={'class': 'border rounded w-full p-2'}),
        }
