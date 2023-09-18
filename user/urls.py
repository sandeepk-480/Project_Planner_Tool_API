from django.contrib import admin
from django.urls import path
from user.views import UserBase

urlpatterns = [
    path('',UserBase.as_view(), name='all_users'),
    path('<int:id>/',UserBase.as_view(), name='specific_user'),
]