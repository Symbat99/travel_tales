from django.urls import path
from django.contrib import admin
from post.views import index_view, post_create_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='main'),
    path('create/', post_create_view, name='post_create')
]




