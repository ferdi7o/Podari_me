from django.db import models

class Profile(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=20)
    profile_picture = models.URLField(blank=True, null=True) # the pictures will come from the internet

    def __str__(self):
        return f"{self.first_name} {self.last_name}"