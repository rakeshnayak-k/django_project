from django.shortcuts import render
from rest_framework.views import APIView
import datetime
from expenses.models import Expenses
from income.models import Income
from rest_framework import status, response

# Create your views here.

class ExpenseSummaryStats(APIView):

    def get_catogery(self, expense):
        return expense.category
    
    def get_amount_for_catogery(self, expense_list, category):
        expenses = expense_list.filter(category=category)
        amount = 0
        for expense in expenses:
            amount += expense.amount

        return {'amount' : str(amount)}


    def get(self, request):
        today_date = datetime.date.today()
        ayear_ago = today_date - datetime.timedelta(days=12*30)
        expenses = Expenses.objects.filter(
            owner=request.user, date__gte=ayear_ago, date__lte=today_date)
        final = {}
        catogeries = list(set(map(self.get_catogery,expenses)))

        for expense in expenses:
            for category in catogeries:
                final[category]=self.get_amount_for_catogery(expenses,category)

        return response.Response({'Category_data': final}, status=status.HTTP_200_OK)
    

class IncomeSourcesSummaryStats(APIView):

    def get_sources(self, income):
        return income.source
    
    def get_amount_for_source(self, income_list, source):
        income = income_list.filter(source=source)
        amount = 0
        for i in income:
            amount += i.amount

        return {'amount' : str(amount)}


    def get(self, request):
        today_date = datetime.date.today()
        ayear_ago = today_date - datetime.timedelta(days=12*30)
        income = Income.objects.filter(
            owner=request.user, date__gte=ayear_ago, date__lte=today_date)
        
        final = {}
        sources = list(set(map(self.get_sources,  income)))

        for i in income:
            for source in sources:
                final[source]=self.get_amount_for_source(income,source)

        return response.Response({'Income_Sources_data': final}, status=status.HTTP_200_OK)

