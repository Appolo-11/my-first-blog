from django import forms

from .models import AccessTable

class AccessTableForm(forms.ModelForm):

    class Meta:
        model = AccessTable
        fields = ('name', 'last_name', 'laptop_number', 'laptop_status', 'sap_id',)

    def __init__(self, *args, **kwargs):
        super(AccessTableForm, self).__init__(*args, **kwargs)
        self.fields['sap_id'].required = False


