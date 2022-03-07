from django.urls import path
from bot.views import bott
urlpatterns = [
    path('',bott),
]
