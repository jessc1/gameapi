from itertools import product
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import  Product, Order, OrderItems, Cart, Cartitems


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [  "name", "price","score", "image"] 

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [  "name", "price","score", "image"] 



class OrderItemsSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = OrderItems
        fields = '__all__'
    

class OrderItemsCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItems
        fields = ['order', 'quantity', 'price']
    
    def create(self, validated_data):        
        order_items = OrderItems(
            order=validated_data['order'],
            quantity = validated_data['quantity'],
            price = validated_data['price']
        )


class OrderSerializer(serializers.ModelSerializer):    

    class Meta:
        model = Order
        fields = '__all__'


class OrderUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:        
        model = Cart
        fields = ['num_of_items','cart_total', 'cart_checkout', 'freight']


class CartItemsSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=False)
    class Meta:
        model = Cartitems
        fields = '__all__'

class CartItemsDeleteSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'



