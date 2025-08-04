from .models import *
from django import forms
class prod_form(forms.ModelForm):
    class Meta:
        model=prod_model
        fields='__all__'
        # fields=['name','price','category','description']
