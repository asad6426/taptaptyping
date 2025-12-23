from django.shortcuts import render

# Create your views here.
# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from .forms import SignUpForm, LoginForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect('login')  # Redirect to a home page or dashboard
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('start_test')  # Redirect to a home page or dashboard
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logoutP(request):
    logout(request)
    return redirect('login')