from django import forms
from .models import Event

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
