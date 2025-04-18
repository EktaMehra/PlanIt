from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Booking
from django.contrib.auth.decorators import login_required
from django.db.models import Q  # For complex queries
from django.contrib import messages
from django.core.paginator import Paginator
from .forms import BookingForm, EventForm


# Create your views here.

def home(request):
    query = request.GET.get('q', '').strip()
    events = Event.objects.all()

    # Filter events based on the search query (by name or category)
    if query:
        events = events.filter(Q(name__icontains=query) | Q(category__icontains=query))

    # Paginate events (4 events per page)
    paginator = Paginator(events, 4)  # 4 events per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Pass both page_obj and query to the context
    context = {
        'page_obj': page_obj,
        'query': query,
    }

    return render(request, 'events/home.html', context)


@login_required
def event_list(request):
    events = Event.objects.filter(created_by=request.user)
    return render(request, 'events/event_list.html', {'events': events, 'my_events': True})


# Event CRUD views
@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            print("Event form is valid. Creating event.")
            event = form.save(commit=False)
            event.created_by = request.user  # Ensure 'created_by' is a field in the Event model
            event.save()
            messages.success(request, "Yay!! Your Event has been created successfully!")  # success message for creating event
            return redirect('event_list')  # Redirect to the list of events
    else:
        print("Rendering empty event form.")
        form = EventForm()
    return render(request, 'events/event_form.html', {'form': form})


@login_required
def event_update(request, id):
    event = get_object_or_404(Event, id=id, created_by=request.user)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, "Fab! You have successfully updated your event!")  # success message for creating event
            return redirect("event_list")
    else:
        form = EventForm(instance=event)
    return render(request, 'events/event_form.html', {'form': form, 'action': 'Update'})


@login_required
def event_delete(request, id):
    event = get_object_or_404(Event, id=id, created_by=request.user)
    if request.method == 'POST':
        event.delete()
        return redirect('home')
    return render(request, 'events/event_confirm_delete.html', {'event': event})


# Event detail view for public access
def event_detail(request, id):
    event = get_object_or_404(Event, id=id)
    booking_form = BookingForm()

    if request.method == 'POST' and not (event.created_by == request.user):
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.event = event
            booking.save()
            messages.success(request, "Booking successful!")
            return redirect('booking_confirmation', event_id=event.id)
        else:
            messages.error(request, "Booking failed. Please correct the errors below.")

    return render(request, 'events/event_detail.html', {
        'event': event,
        'booking_form': booking_form,
    })


# Booking confirmation view
def booking_confirmation(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    booking = event.bookings.last()  # Retrieve the last booking
    return render(request, 'events/booking_confirmation.html', {
        'event': event,
        'booking': booking,
    })
