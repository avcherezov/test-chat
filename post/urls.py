from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path('chat/<username>/', views.chat, name="chat"),
    path('no_user/', views.index, name="no_user"),
    path('chat/<username>/message/', views.add_message, name="message")
] 
