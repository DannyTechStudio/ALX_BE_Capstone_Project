from django.db import models
from django.conf import settings

# Create your models here.
class Income(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(blank=True)
    source = models.CharField(max_length=200, blank=False, null=False)
    amount = models.DecimalField(max_digits=14, decimal_places=2)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='incomes'
    )
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Income: {self.title}, Amount: {self.amount}, Owner: {self.owner}"