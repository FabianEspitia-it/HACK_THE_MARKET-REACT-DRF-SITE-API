from django.urls import path

from .views import ShoppingProductAPIView

urlpatterns = [
    path('shopping_cart/<int:pk>', ShoppingProductAPIView.as_view(), name = 'shopping_cart' )
]