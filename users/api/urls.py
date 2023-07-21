from django.urls import path

from .views import UserAPIView, CreateUserAPIView

urlpatterns = [
    path('user/<int:pk>', UserAPIView.as_view(), name= 'user'),
    path('create_user/', CreateUserAPIView.as_view(), name= 'user_create')
]
