from django.shortcuts import render, get_object_or_404, redirect
from .models import Event
from .forms import EventForm
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

@login_required
def event_update(request, pk):
    print(f"Accessing update view for event ID: {pk}")
    event = get_object_or_404(Event, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            print("Event form is valid. Updating event.")
            form.save()
            return redirect('event_list')
    else:
        print("Rendering event form with existing data.")
        form = EventForm(instance=event)
    return render(request, 'events/event_form.html', {'form': form})

@login_required
def event_delete(request, pk):
    print(f"Accessing delete view for event ID: {pk}")
    event = get_object_or_404(Event, pk=pk, created_by=request.user)
    if request.method == 'POST':
        print("Deleting event.")
        event.delete()
        return redirect('event_list')
    return render(request, 'events/event_confirm_delete.html', {'event': event})


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
            return redirect('event_list')  # Redirect to the list of events
    else:
        print("Rendering empty event form.")
        form = EventForm()
    return render(request, 'events/event_form.html', {'form': form})
