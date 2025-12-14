from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    
    class Meta:
        model = Category
        fields = ['id', 'name', 'owner']
       