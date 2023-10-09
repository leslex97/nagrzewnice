from django import forms
from devices.models import Switches, DeviceType

class SearchForm(forms.Form):
    fraze = forms.CharField(
        required= False,
        max_length= 20,
        strip = True,
        label='Fraza')
    
    switches = forms.ModelChoiceField(
        required=False,
        queryset=Switches.objects.all(),
        label='Przełącznik')

    type_of_device = forms.ModelChoiceField(
        
        required=False,
        queryset= DeviceType.objects.all(),
        label='Typ urządzenia')
