from django.shortcuts import render
from .models import AccessTable

def access_table_list(request):
	users = AccessTable.objects.order_by('name')	
	return render(request, 'philipp_app/access_table_list.html', {'users': users})
def access_laptop_list(request):
	users = AccessTable.objects.order_by('name')
	return render(request, 'philipp_app/access_table_list.html', {'users': users})
def menu(request):
	return render(request, 'philipp_app/menu.html')