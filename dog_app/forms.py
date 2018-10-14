from django import forms
from dog_app.models import *

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('file', )