from django import forms 
from django.contrib.auth.models import User
from vendor.models import *
class SelectItemForm(forms.ModelForm):
    class Meta:
        model = SelectProduct
        fields = ['user','product','vendor','quantity']
        widgets = {'quantity':forms.NumberInput(attrs={'class':'form-control'})}