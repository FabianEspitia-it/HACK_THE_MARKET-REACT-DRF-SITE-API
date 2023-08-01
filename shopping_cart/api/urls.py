from django.urls import path

from .views import ShoppingCartAPIView

urlpatterns = [
    path('shopping_cart/<int:pk>',ShoppingCartAPIView.as_view(), name = 'shopping_cart' )
]