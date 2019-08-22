from .models import *
from django import forms
from django.db import models
from rasberrypy.models import Product


class ProductionConfigure(forms.ModelForm):
    timeConfigure = forms.IntegerField(default=30,null=False)
    mode = forms.BooleanField(default=False)
    timeConfigure.widget.attrs.update({'class' : 'form-control'})
    class Meta:
        model = Product

    def clean_timeConfigure(self):
        data = self.cleaned_data["timeConfigure"]
        return data

    def clean_mode(self):
        data = self.cleaned_data["mode"]
        return data

