from django.urls import path
from .views import *

urlpatterns = [
    path('', data_all, name='all_data'),
]
