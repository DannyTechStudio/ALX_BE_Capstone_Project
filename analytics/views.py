from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.db.models import Sum
from django.utils import timezone

from income.models import Income
from expense.models import Expense


# Create your views here.
class AnalyticsView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        # Get user
        user = request.user
        
        # Fetch data
        incomes = Income.objects.filter(owner=user)
        expenses = Expense.objects.filter(owner=user)
        
        # Calculate totals
        total_income = incomes.aggregate(total=Sum('amount'))['total'] or 0
        total_expense = expenses.aggregate(total=Sum('amount'))['total'] or 0
        
        # Calculate balance
        balance = total_income - total_expense
        
        # Group expenses by category
        category_totals = (
            expenses
            .values('category__id', 'category__name')
            .annotate(total_spent=Sum('amount'))
            .order_by('-total_spent')[:3]
        )
        
        # Accumulate response
        response_data = {
            "total_income": total_income,
            "total_expense": total_expense,
            "balance": balance,
            "top_categories": category_totals
        }
        
        # Return response
        return Response(response_data) 
    

class MonthlySummaryView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        user = request.user
        
        # Getting user request's year & month
        month = request.query_params.get('month')
        year = request.query_params.get('year')
        
        now = timezone.now()
        
        # Conversion
        try:
            month = int(month) if month else None
            year = int(year) if year else None
        except ValueError:
            return Response(
                {"error": "Month and year must be integers"},
                status=400
            )
        
        # Year provided but in the future
        if year and year > now.year:
            return Response(
                {"error": "Year must not be in the future."}, 
                status=400
            )
        
        # Other validations and assignments
        if not month and not year:
            target_month = now.month
            target_year = now.year      # Both year & month not provided
        elif year and not month:
            target_month = now.month
            target_year = year          # Year provided but month not provided
        elif not year and month:
            target_month  = month
            target_year = now.year      # Year not provided but month provided
        else:
            target_month = month
            target_year = year          # Both year & month are provided
            
        # Invalid date number
        if target_month < 1 or target_month > 12:
            return Response(
                {"error": "Month must be less than 1 or greater than 12"},
                status=400
            )
            
        # Getting all income instances
        incomes = Income.objects.filter(owner=user, date__year=target_year, date__month=target_month)
        
        # Getting all expense instances
        expenses = Expense.objects.filter(owner=user, date__year=target_year, date__month=target_month)
        
        # Calculate totals
        monthly_income = incomes.aggregate(total=Sum('amount'))['total'] or 0
        monthly_expense = expenses.aggregate(total=Sum('amount'))['total'] or 0
        
        # Calculate monthly balance
        monthly_balance = monthly_income - monthly_expense
        
        # Top 3 spending categories
        top_spending_categories = expenses.values('category__id', 'category__name').annotate(total_spent=Sum('amount')).order_by('-total_spent')[:3]
        
        # Preparing response data
        response_data = {
            "Year": target_year,
            "Month": target_month,
            "Total monthly incomes": monthly_income,
            "Total monthly expenses": monthly_expense,
            "Monthly balance": monthly_balance,
            "Top 3 spending categories": top_spending_categories
        }
        
        return Response(response_data)