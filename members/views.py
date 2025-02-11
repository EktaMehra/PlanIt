from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.contrib.auth.models import User


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


# Username validation view (AJAX)
def check_username(request):
    username = request.GET.get("username", None)
    if username and User.objects.filter(username=username).exists():
        return JsonResponse({"is_taken": True})
    return JsonResponse({"is_taken": False})


class EventOrganizerLoginView(LoginView):
    template_name = 'members/login.html'  # event organizers custom template
