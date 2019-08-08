from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.blogs, name='blog'),
    path('<int:blog_id>', views.detail, name='detail')
]
