from django.db import models
from django.conf import settings
from category.models import Category

# Create your models here.
class Expense(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField()
    amount = models.DecimalField(max_digits=14, decimal_places=2, blank=False, null=False)
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        blank=False,
        null=False, 
        related_name='categories'
    )
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='expenses')
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date']
    
    def __str__(self):
        return f"Expense: {self.title}, Category: {self.category}, Amount: {self.amount}, Owner: {self.owner}"