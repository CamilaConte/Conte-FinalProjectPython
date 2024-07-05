from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as django_login
from users.forms import RegisterForm, EditProfileForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from users.models import ExtraUserData

def login(request):
    form = AuthenticationForm()
    
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            
            user = authenticate(username=username, password=password)
            django_login(request, user)
            
            ExtraUserData.objects.get_or_create(user=user)
            
            return redirect("home")
            
    return render(request, 'users/login.html', {"form": form})

def register(request):
    form = RegisterForm()
    
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    
    return render(request, 'users/register.html', {"form": form})

@login_required
def profile(request):
    return render(request, 'users/profile.html', {})

@login_required
def password_success(request):
    return render(request, 'users/password_success.html', {})

@login_required
def edit_profile(request):
    form = EditProfileForm(initial={"avatar": request.user.extrauserdata.avatar, "birth_date":request.user.extrauserdata.birth_date}, instance=request.user)
    
    if request.method == "POST":
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            extra_data = request.user.extrauserdata
            extra_data.avatar = form.cleaned_data.get("avatar")
            extra_data.birth_date = form.cleaned_data.get("birth_date")
            extra_data.save()
            form.save()
            return redirect('profile')
        
    return render(request, 'users/edit_profile.html', {"form": form})

class ChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = "users/change_password.html"
    success_url = reverse_lazy("password_success")
