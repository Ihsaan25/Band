from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .forms import ExtendedUserCreationForm 
from django.contrib import messages

# Create your views here.
def user_login(request):
    return render(request, 'authentication/login_page.html')

def authenticate_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in successfully!')
            return HttpResponseRedirect(reverse('user_auth:show_user'))
        else:
            messages.error(request, 'Invalid username or password.')
    return HttpResponseRedirect(reverse('user_auth:login'))
    
def show_user(request):
    return render(request, 'pages/index.html' )

def register(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_auth:login')  # Redirect to the main page after registration
        else:
            print("Form is not valid. Errors:", form.errors)
    else:
        form = ExtendedUserCreationForm()

    return render(request, 'authentication/user_registration.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully!')
    return redirect('pages:index')
