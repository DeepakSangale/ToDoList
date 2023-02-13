from django import forms
from .models import ModelClass
from django.forms import ModelForm

class TaskForm(forms.ModelForm):
    class Meta():
        model=ModelClass
        fields="__all__"
    