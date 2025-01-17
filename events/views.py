from django.shortcuts import render
from .models import Event
from .forms import EventForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    print("Home page accessed.")
    return render(request, 'events/home.html')


@login_required
def event_detail(request, pk):
    print(f"Accessing details for event ID: {pk}")
    event = get_object_or_404(Event, pk=pk, created_by=request.user)
    return render(request, 'events/event_detail.html', {'event': event})

@login_required
def event_list(request):
    print("Event list accessed.")
    events = Event.objects.filter(created_by=request.user)
    return render(request, 'events/event_list.html', {'events': events})

@login_required
def event_create(request):
    print("Event creation view accessed.")
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            print("Event form is valid. Creating event.")
            event = form.save(commit=False)
            event.created_by = request.user
            event.save()
            return redirect('event_list')
        else:
            print("Rendering empty event form.")
            form = EventForm()
        return render(request, 'events/event_form.html', {'form': form})


