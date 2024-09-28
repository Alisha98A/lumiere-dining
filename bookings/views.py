from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm

# View function to handle user signup, including form validation and user login
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('home')  
    else:
        form = SignUpForm()
    return render(request, 'bookings/signup.html', {'form': form})

# Returns a welcome message for the home page.
def home_view(request):
    return HttpResponse("Welcome to the restaurant booking system!")