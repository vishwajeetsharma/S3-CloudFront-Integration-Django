from django import forms
from .models import datas

class ImageForm(forms.ModelForm):
    class Meta:
        model=datas
        fields=("name","image")

class FileForm(forms.ModelForm):
    class Meta:
        model=datas
        fields=("name","image")