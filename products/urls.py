from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'products', views.ProductsViewSet, basename='products'),
router.register(r'orders', views.OrderViewSet, basename='orders'),
router.register(r'ordersitems', views.OrderItemsViewSet, basename='ordersitems')
router.register(r'cartitems', views.CartItemsViewSet, basename="cartitems")
router.register(r'cart', views.CartViewSet, basename="cart")
router.register(r'detail', views.CartItemDeleteViewSet, basename="detail")



urlpatterns = [
    path('product/<int:pk>/', views.ProductDetail.as_view()),
        

]
urlpatterns = router.urls