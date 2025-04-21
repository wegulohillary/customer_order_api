from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.utils import timezone
from .models import Customer, Order
from unittest.mock import patch

class CustomerOrderAPITests(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.customer_data = {
            "name": "Alice Smith",
            "code": "CUST001"
        }
        self.order_data = {
            "item": "Laptop",
            "amount": 950.00,
        }

    def test_create_customer(self):
        response = self.client.post(reverse('customer-list'), self.customer_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 1)
        self.assertEqual(Customer.objects.get().name, 'Alice Smith')

    def test_list_customers(self):
        Customer.objects.create(**self.customer_data)
        response = self.client.get(reverse('customer-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    @patch('orders.utils.send_sms_alert')  # Assuming your SMS function is in orders/utils.py
    def test_create_order_with_sms(self, mock_send_sms):
        customer = Customer.objects.create(**self.customer_data)
        order_payload = {
            "customer": customer.id,
            "item": "Phone",
            "amount": 300.0
        }
        response = self.client.post(reverse('order-list'), order_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)
        mock_send_sms.assert_called_once()

    def test_create_order_invalid(self):
        response = self.client.post(reverse('order-list'), {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_order_list(self):
        customer = Customer.objects.create(**self.customer_data)
        Order.objects.create(customer=customer, item="Keyboard", amount=50.0, timestamp=timezone.now())
        response = self.client.get(reverse('order-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
