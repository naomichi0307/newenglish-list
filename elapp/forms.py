from django import forms
from .models import elModel, Newword
from django.forms import ModelForm

class VenueForm(ModelForm):
    class Meta:
        model = Newword
        fields = ('word',)