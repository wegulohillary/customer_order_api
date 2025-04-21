from django.contrib import admin
from .models import Customer, Order

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code')
    search_fields = ('name', 'code')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'item', 'amount', 'timestamp')
    list_filter = ('timestamp',)
    search_fields = ('item', 'customer__name')
