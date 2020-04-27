from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from  rest_framework import generics
from orders.models import SalesOrder
from orders.serialaizers import OrderSerialaizer


def order_page(request):
    return render(request, 'index.html', {'orders': SalesOrder.objects.all()})

class OrderView(ModelViewSet):
    queryset = SalesOrder.objects.all()
    serializer_class = OrderSerialaizer

def order_app(request):
    return render(request, 'main_app.html')