from django.forms import ModelForm
from .models import Car

class carform(ModelForm):
    class Meta:
        model=Car
        fields='__all__'


