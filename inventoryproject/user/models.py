from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    staff = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=255)
    image = models.ImageField(default='avatar.jpg', upload_to='profile_images/')

    def __str__(self) -> str:
        return f"{self.staff.username}'s Profile"