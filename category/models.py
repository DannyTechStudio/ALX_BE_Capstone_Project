from django.db import models
from django.conf import settings

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='categories')
    
    # Prevent duplicate category names for the same user
    class Meta:
        unique_together = ['name', 'owner']
    
    def __str__(self):
        return f"Category: {self.name} (User: {self.owner.email})"