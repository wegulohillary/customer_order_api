from rest_framework import viewsets
from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer
from rest_framework.response import Response
from rest_framework import status
import africastalking

# Africa's Talking config
africastalking.initialize(username='sandbox', api_key='your_api_key')
sms = africastalking.SMS

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        order = serializer.save()
        phone = "+2547xxxxxxxx"  # Ideally from the Customer model
        message = f"Order received: {order.item} for {order.amount}"
        sms.send(message, [phone])
