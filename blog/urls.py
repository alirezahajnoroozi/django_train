from django.urls import path, include
from .views import blog_home, blog_single, test

app_name = 'blog'

urlpatterns = [
    path('', blog_home, name='home'),
    path('single', blog_single, name='single'),
    path('<int:pid>', test, name='test')
]