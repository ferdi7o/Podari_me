from django.db import models
from gifts.models import Gift
from accounts.models import Profile

class Comment(models.Model):
    gift = models.ForeignKey(Gift, on_delete=models.CASCADE, related_name='comments')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    content = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.profile.first_name} on {self.gift.title}"


class Favorite(models.Model):
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    gifts = models.ManyToManyField(Gift)