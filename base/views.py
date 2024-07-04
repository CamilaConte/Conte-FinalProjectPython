from django.shortcuts import redirect, render

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'base/about_me.html', {})