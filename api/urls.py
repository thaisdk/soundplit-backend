from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include

from api import views

urlpatterns = [
    # path('list_users/', views.get_all_users),
    # path('user/add/', views.add_users),
]
