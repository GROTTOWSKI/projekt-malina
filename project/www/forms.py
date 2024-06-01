from django import forms
from .models import Marka, Typ, Osprzęt, Model


class MarkaForm(forms.ModelForm):
    class Meta:
        model = Marka
        fields = '__all__'


class TypForm(forms.ModelForm):
    class Meta:
        model = Typ
        fields = '__all__'


class OsprzętForm(forms.ModelForm):
    class Meta:
        model = Osprzęt
        fields = '__all__'

class ModelForm(forms.ModelForm):
    class Meta:
        model = Model
        fields = '__all__'