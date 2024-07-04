from django import forms

class SearchPatients(forms.Form):
    last_name = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={"class":"form-control"}))