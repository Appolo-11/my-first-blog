from django.urls import path
from . import views

urlpatterns = [
    path('', views.access_table_list, name='access_table_list'),
]
