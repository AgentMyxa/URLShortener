from django.urls import path
from . import views

urlpatterns = [
    path('createlink/', views.create_link),
    path('', views.index),
    path('<str:id>', views.redirect),
]