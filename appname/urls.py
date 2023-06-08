from django.contrib import admin
from django.urls import path,include

from . import views
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
urlpatterns = [
    path("sendMessage/",views.Send_Message,name='sendMessage'),
    path("login/",views.login_view,name="login"),
    path("register/",views.register,name="register"),
    path('token/',MyTokenObtainPairView.as_view(),name="token_obtain_pair"),
    path('token/refresh/',TokenRefreshView.as_view(),name="token_refresh"),
]
