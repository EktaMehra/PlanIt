from django.shortcuts import render

# Create your views here.
def home(request):
    print("Home page accessed.")
    return render(request, 'events/home.html')
