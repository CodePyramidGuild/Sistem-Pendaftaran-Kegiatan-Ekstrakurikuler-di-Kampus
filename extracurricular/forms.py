from django import forms
from .models import Kegiatan

class FormKegiatan(forms.ModelForm):
    class Meta:
        model = Kegiatan
        fields = '__all__'
