from django.shortcuts import render
from .models import AccessTable
from .forms import AccessTableForm

def access_table_list(request):
	users = AccessTable.objects.order_by('last_name')	
	return render(request, 'philipp_app/access_table_list.html', {'users': users})
def access_laptop_list(request):
	users = AccessTable.objects.order_by('last_name')
	return render(request, 'philipp_app/access_laptop_list.html', {'users': users})
def menu(request):
	return render(request, 'philipp_app/menu.html')
def new_user(request):
	form = AccessTableForm()
	return render(request, 'philipp_app/user_edit.html', {'form': form})


