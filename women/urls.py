from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'), #http://localhost:8000/women/
    path('cats/<int:catid>/', categories), #http://localhost:8000/women/cats
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive)
]