from django import forms

from .models import AccessTable

class AccessTableForm(forms.ModelForm):

    class Meta:
        model = AccessTable
        fields = ('name', 'last_name', 'laptop_number', 'laptop_status', 'sap_id',)

    def __init__(self, *args, **kwargs):
        super(AccessTableForm, self).__init__(*args, **kwargs)
        self.fields['sap_id'].required = False

    def clean(self):
        cleaned_data = super(AccessTableForm, self).clean()
        name = cleaned_data.get("name")
        last_name = cleaned_data.get("last_name")
        sap_id = cleaned_data.get("sap_id")

        if len(AccessTable.objects.filter(name=name).filter(last_name=last_name)) > 1:
            # Only do something if there are two users with same names
            if not sap_id: 
                self._errors["sap_id"] = self.error_class(["Please, fill the field."])
                raise forms.ValidationError("There are more than one users with such name. "
                        "Please, enter the SAP ID.")
        elif len(AccessTable.objects.filter(name=name).filter(last_name=last_name)) == 0:
            raise forms.ValidationError("There is no user with such name and/or last name. "
                         "Please, enter correct parameters.")

        if sap_id and len(AccessTable.objects.filter(name=name).filter(last_name=last_name).filter(sap_id=sap_id)) == 0:
            raise forms.ValidationError("There is no user with such SAP ID. "
                         "Please, enter correct parameters.")
            

        # Always return the full collection of cleaned data.
        return cleaned_data




