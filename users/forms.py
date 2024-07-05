from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}))
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class":"form-control", "type":"password"}))
    password2 = forms.CharField(label="Repeat password", widget=forms.PasswordInput(attrs={"class":"form-control", "type":"password"}))
    
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]
        help_texts = {key: "" for key in fields}

#TODO: agregar avatar y datos extra        
class EditProfileForm(UserChangeForm):
    password = None
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    avatar = forms.ImageField(required=False)
    birth_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"class":"form-control"}))
    
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "avatar", "birth_date"]

class PasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label="Old password", widget=forms.PasswordInput(attrs={"class":"form-control", "type":"password"}))
    new_password1 = forms.CharField(label="New password", widget=forms.PasswordInput(attrs={"class":"form-control", "type":"password"}))
    new_password2 = forms.CharField(label="Confirm new password", widget=forms.PasswordInput(attrs={"class":"form-control", "type":"password"}))
    
    class Meta:
        model = User
        fields = ["old_password", "new_password1", "new_password2"]