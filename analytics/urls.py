from django.urls import path
from .views import AnalyticsView, MonthlySummaryView

urlpatterns = [
    path('overall/', AnalyticsView.as_view(), name='overall-analytics'),
    path('summary/', MonthlySummaryView.as_view(), name='monthly-summary')
]
