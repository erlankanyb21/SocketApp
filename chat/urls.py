from django.urls import path
from . import views
from .api import SendMessageAPI

urlpatterns = [
    path('', views.index, name='index'),
    path('chat/', views.chat, name='chat'),
]

