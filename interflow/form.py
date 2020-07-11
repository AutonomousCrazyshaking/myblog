from django import forms
from .models import Board


class InterflowModelForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = '__all__'