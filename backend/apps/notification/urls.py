# backend/apps/notification/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('notifications/', views.notification_list, name='notification_list'),
]
