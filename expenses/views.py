from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Expense
from expenses.templates.serializer import ExpenseSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.http import JsonResponse
import json
from decimal import Decimal
from datetime import date, datetime


class ExpenseList(ListView):
    model = Expense

class ExpenseDetails(DetailView):
    model = Expense

class ExpenseCreate(CreateView):
    model = Expense
    #template_name = "expenses/expense_form.html"
    fields = ['name', 'type', 'place', 'amount', 'date']
    success_url = reverse_lazy('expense_list')

class ExpenseUpdate(UpdateView):
    model = Expense
    # template_name = "expenses/expense_form.html"
    fields = ['name', 'type', 'place', 'amount', 'date']
    success_url = reverse_lazy('expense_list')

class ExpenseDelete(DeleteView):
    model = Expense
    success_url = reverse_lazy('expense_list')

def show(request):
    object_list = Expense.objects.all()
    return render(request,"expenses/show.html",{'object_list':object_list})

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)


@api_view(['GET', 'POST'])
def hello_world(request):
    object_list = Expense.objects.all().values('name', 'type', 'place', 'amount', 'date')
    if request.method == 'POST':
        return JsonResponse({"message": "Got some data!", "data": request.data})
    return JsonResponse(json.dumps(list(object_list), cls=DecimalEncoder), safe=False)