from django.urls import path
from . import views

urlpatterns = [
	path('', views.menu),
    path('access_table', views.access_table_list, name='access_table_list'),
    path('laptop', views.access_laptop_list, name='access_laptop_list')
]
