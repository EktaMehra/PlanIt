from django.shortcuts import render, get_object_or_404, redirect
from .models import Event
from .forms import EventForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q  # For complex queries
from django.contrib import messages
from django.core.paginator import Paginator


# Create your views here.

# Home view with search functionality and pagination
def home(request):
    query = request.GET.get('q', '').strip()
    events = Event.objects.all()

    # Filter events by name based on search query
    if query:
        events = events.filter(name__icontains=query)

    # Paginate the events
    paginator = Paginator(events, 5)  # Show 5 events per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'events/home.html', {
        'page_obj': page_obj,
        'query': query,
    })



@login_required
def event_list(request):
    events = Event.objects.filter(created_by=request.user)
    return render(request, 'events/event_list.html', {'events': events})


# Event CRUD views
@login_required
def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            print("Event form is valid. Creating event.")
            event = form.save(commit=False)
            event.created_by = request.user  # Ensure 'created_by' is a field in the Event model
            event.save()
            messages.success(request, 'Event created successfully!')
            return redirect('event_list')  # Redirect to the list of events
    else:
        print("Rendering empty event form.")
        form = EventForm()
        
    return render(request, 'events/event_form.html', {'form': form})


@login_required
def event_update(request, pk):
    event = get_object_or_404(Event, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EventForm(instance=event)
    return render(request, 'events/event_form.html', {'form': form, 'action': 'Update'})

@login_required
def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk, created_by=request.user)
    if request.method == 'POST':
        event.delete()
        return redirect('home')
    return render(request, 'events/event_confirm_delete.html', {'event': event})


@login_required
def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk, created_by=request.user)
    return render(request, 'events/event_detail.html', {'event': event})
