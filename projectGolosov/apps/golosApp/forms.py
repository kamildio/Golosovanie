from django.views.generic import UpdateView
from django import forms
from .models import CanditeForm

class CreateCandiForm(forms.ModelForm):
    class Meta:
        model = CanditeForm
        fields = ['first_name', 'last_name', 'bio', 'birthdate', 'image', 'partiya']

class CanditeFormEditForm(forms.ModelForm):
    class Meta:
        model = CanditeForm
        fields = ['first_name', 'last_name', 'bio', 'birthdate', 'image', 'partiya']