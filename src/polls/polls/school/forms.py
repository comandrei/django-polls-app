from django import forms

from .models import Client, Reprezentant

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = "__all__"
    

class ReprezentantForm(forms.ModelForm):
    class Meta:
        model = Reprezentant
        exclude = []