from rest_framework import viewsets, permissions, filters
from .models import Income
from .serializers import IncomeSerializer

# Create your views here.
class IncomeViewSet(viewsets.ModelViewSet):
    serializer_class = IncomeSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['date']
    search_fields = ['title']
    
    def get_queryset(self):
        return Income.objects.filter(owner=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)