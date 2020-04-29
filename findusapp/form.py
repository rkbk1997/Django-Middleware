from django import forms
from findusapp.models import *

class CateForm(forms.ModelForm):
    class Meta:
        model=Cate
        fields="__all__"

class SubcateForm(forms.ModelForm):
    class Meta:
        model=Subcate
        fields="__all__"