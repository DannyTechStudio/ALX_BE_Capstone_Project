from rest_framework import serializers
from .models import Expense

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['id', 'title', 'amount', 'category', 'owner', 'date']
        ordering_field = ['date']
        search_fields = ['title']
        read_only_fields = ['owner', 'date']