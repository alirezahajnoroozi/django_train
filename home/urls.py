from django.urls import path, include
from .views import home,blog,about

urlpatterns = [
    path('', home),
    path('blog', blog),
    path('about', about),
]