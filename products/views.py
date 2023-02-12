from rest_framework import viewsets, permissions, generics, status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets, permissions
from .serializers import ProductSerializer, OrderUpdateSerializer, OrderSerializer, OrderItemsSerializer, CartSerializer, CartItemsSerializer, CartItemsDeleteSerializer, ProductDetailSerializer
from .models import  Product, OrderItems, Order, Cart, Cartitems
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend

class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'price', 'score']


class ProductDetail(APIView):
   
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'paid']

    

class OrderItemsViewSet(viewsets.ModelViewSet):
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemsSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]

class CartItemsViewSet(viewsets.ModelViewSet):
    queryset = Cartitems.objects.all()
    serializer_class = CartItemsSerializer
    permission_classes = [permissions.IsAuthenticated]    
        

class CartItemDetail(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer

class CartItemDeleteViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = CartItemsDeleteSerializer

    def destroy(self, request, pk=None, *args, **kwargs):
        instance = self.get_object()
        return super(CartItemDeleteViewSet, self).destroy(request, pk, *args, **kwargs)    
        








