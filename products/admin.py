from django.contrib import admin
from .models import *

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'price')
    search_fields = ('name',)

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("num_of_items", "cart_total", "cart_checkout", "freight")



@admin.register(Cartitems)
class CartItemsAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', "cart_id")

    
admin.site.register(Customer)
admin.site.register(SavedItem)
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("customer", "paid", "id", "cart_id")    
    date_hierarchy = 'created'
    ordering = ('-created',)

admin.site.register(OrderItems)
