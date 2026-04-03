from django.db import models
from django.contrib.auth.models import User 


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location_found = models.CharField(max_length=255)
    date_reported = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50, default='Found')  # Default status
    image = models.ImageField(upload_to="items/", blank=True, null=True)

    #link to the user
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reported_items')

    def __str__(self):
        return self.name


class Claim(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    verification_text = models.TextField()  # The "How do you know it's yours?" field from your wireframe
    claim_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='Pending')  # Pending/Approved/Rejected

    def __str__(self):
        return f"{self.user.username} - {self.item.name}"