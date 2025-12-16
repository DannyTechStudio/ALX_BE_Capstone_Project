from rest_framework import viewsets, permissions, filters
from .models import Expense
from .serializers import ExpenseSerializer

# Create your views here.
class ExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['date', 'amount']
    
    def get_queryset(self):
        return Expense.objects.filter(owner=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
