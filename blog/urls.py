from django.urls import path, include
from .views import blog_home, blog_single

app_name = 'blog'

urlpatterns = [
    path('', blog_home, name='home'),
    path('single', blog_single, name='single'),
]