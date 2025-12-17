from rest_framework import serializers
from .models import Income

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ['id', 'title', 'source', 'amount', 'owner', 'date']
        read_only_fields = ['owner', 'date']