from django.urls import path, include
from .views import index,blog,about

urlpatterns = [
    path('', index),
    path('blog', blog),
    path('about', about),
]