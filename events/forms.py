from django import forms
from .models import Booking, Event


class EventForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'class': 'form-control'})
    )
    time = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time', 'class': 'form-control', 'placeholder': 'HH:MM'}),
    )

    class Meta:
        model = Event
        fields = ['name', 'date', 'description', 'category', 'location', 'time']


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Email is required.")
        return email
