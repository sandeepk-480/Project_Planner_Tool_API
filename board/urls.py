from django.contrib import admin
from django.urls import path
from board.views import ProjectBoardBase

urlpatterns = [
    path('', ProjectBoardBase.as_view(), name='allboard'),
    path('<int:id>', ProjectBoardBase.as_view(), name='specificboard')
]