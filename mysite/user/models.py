from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to='images/_profile')
    phone_number = models.CharField(max_length=50, default='+213 123456789')

    def __str__(self) -> str:
        return self.user.username
