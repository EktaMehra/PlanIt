from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

# Registration view

def register(request):
    print("Registration view accessed.")
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print("Processing POST request for registration.")
        if form.is_valid():
            print("Registration form valid. Saving new user.")
            form.save()
            return redirect('login')
    else:
        print("Rendering empty registration form.")
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
