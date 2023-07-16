from django.urls import path
from .views import post_create_view

urlpatterns = [
    path('/create', post_create_view, name = 'post_create')
]