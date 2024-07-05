from django import forms
from patients.models import Patient

class SearchPatientsForm(forms.Form):
    last_name = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={"class":"form-control"}))
    
class CreatePatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ("name", "last_name", "document", "phone_number", "last_xray", "birth_date", "observations")
        
        widgets = {
            "name": forms.TextInput(attrs={"class":"form-control"}),
            "last_name": forms.TextInput(attrs={"class":"form-control"}),
            "document": forms.TextInput(attrs={"class":"form-control"}),
            "phone_number": forms.TextInput(attrs={"class":"form-control"}),
            "birth_date": forms.TextInput(attrs={"class":"form-control"}),
            "observations": forms.Textarea(attrs={"class":"form-control"}),
        }

class UpdatePatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ("name", "last_name", "phone_number", "birth_date", "last_xray", "observations")
        
        widgets = {
            "name": forms.TextInput(attrs={"class":"form-control"}),
            "last_name": forms.TextInput(attrs={"class":"form-control"}),
            "phone_number": forms.TextInput(attrs={"class":"form-control"}),
            "birth_date": forms.TextInput(attrs={"class":"form-control"}),
            "observations": forms.Textarea(attrs={"class":"form-control"}),
        }