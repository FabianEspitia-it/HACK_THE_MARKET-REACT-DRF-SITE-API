from django.urls import path

from .views import UserAPIView, LoginUserAPIview, RegisterUserAPIView

urlpatterns = [
    path('user/<int:pk>', UserAPIView.as_view(), name= 'user'),
    path('login/', LoginUserAPIview.as_view(), name = "login" ),
    path('register/', RegisterUserAPIView.as_view(), name= 'register')
   
]
