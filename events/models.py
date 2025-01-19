from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    location = models.CharField(max_length=300)
    date = models.DateField()
    time = models.TimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

# Log statement to confirm Event model loading
print("Event model loaded successfully.")