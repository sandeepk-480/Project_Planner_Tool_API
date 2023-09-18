from django.contrib import admin
from django.urls import path
from team.views import TeamBase

urlpatterns = [
    path('',TeamBase.as_view(), name="Team list"),
    path('<int:team_id>/',TeamBase.as_view(), name="Specific Team"),

]