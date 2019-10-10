from django import forms

from .models import AccessTable

class AccessTableForm(forms.ModelForm):

    class Meta:
        model = AccessTable
        fields = ('name', 'last_name', 'laptop_number', 'laptop_status',)

