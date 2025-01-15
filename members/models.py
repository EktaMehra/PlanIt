from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=255)

# Log statement to confirm model loading
print("CustomUser model loaded successfully.")