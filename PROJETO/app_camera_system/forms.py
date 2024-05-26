from django import forms
from .models import Company, CameraPark, Camera

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'

class CameraParkForm(forms.ModelForm):
    class Meta:
        model = CameraPark
        fields = ['name', 'department', 'location']

class CameraForm(forms.ModelForm):
    class Meta:
        model = Camera
        fields = ['specific_location', 'brand', 'model', 'network_stream_protocol', 'ip_address', 'port', 'username', 'password']

