from django import forms
from .models import movie


class movieforms(forms.ModelForm):
    class Meta:
        model = movie
        fields = ['name', 'des', 'year', 'im']