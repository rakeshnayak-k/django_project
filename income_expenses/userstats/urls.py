from .views import ExpenseSummaryStats, IncomeSourcesSummaryStats
from django.urls import path

urlpatterns = [
    path('expenses-catogery-data',ExpenseSummaryStats.as_view(),name='expenses-catogery-summary'),
    path('income-source-data',IncomeSourcesSummaryStats.as_view(),name='income-source-summary'),
]