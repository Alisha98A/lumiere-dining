from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import SignUpForm
from django.utils import timezone 

# View function to handle user signup, including form validation and user login
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('dashboard') 
    else:
        form = SignUpForm()
    return render(request, 'bookings/signup.html', {'form': form})

# Returns a welcome message for the home page.
def home_view(request):
    return render(request, 'bookings/home.html')    


# View function to handle user login
def custom_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')  
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)  
                return redirect('dashboard')  
            else:
                messages.error(request, "Invalid username or password")  
        else:
            messages.error(request, "Invalid username or password")
    else:
        form = AuthenticationForm()

    return render(request, 'bookings/login.html', {"form": form})

@login_required  # Ensure the user is logged in to access the dashboard
def dashboard(request):
    return render(request, 'bookings/dashboard.html')

@login_required  # Ensure the user is logged in to access the dashboard view
def dashboard_view(request):
    return render(request, 'dashboard.html', {'current_year': timezone.now().year})

@login_required
def profile(request):
    """Render the user's profile page, accessible only to authenticated users."""
    return render(request, 'bookings/profile.html')
