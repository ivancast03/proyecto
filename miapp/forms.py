from django import forms
from .models import Dork


class DorkForm(forms.ModelForm):
    class Meta:
        model = Dork
        fields = ["titulo", "dork"]
