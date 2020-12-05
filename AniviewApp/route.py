from django.urls import path

from django.http import HttpResponse

# view
from .views import index

urlpatterns = [
    path('', index, name='index'),
]