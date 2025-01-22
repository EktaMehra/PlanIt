from django import forms
from .models import Event
from .models import Booking

class EventForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'class': 'form-control'})
    )

    class Meta:
        model = Event
        fields = ['name', 'date', 'description', 'category', 'location', 'time', 'created_by']


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone Number'}),
        }