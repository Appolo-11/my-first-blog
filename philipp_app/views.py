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
	if request.method == "POST":
		form = AccessTableForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			if post.name == 'Alex':
				print("Ama ALEX")
			#if len(AccessTable.objects.filter(name=post.name).filter(last_name=post.last_name)) > 1:
			post.card_number = AccessTable.objects.filter(name=post.name).filter(last_name=post.last_name)[0].card_number
			post.sap_id = AccessTable.objects.filter(name=post.name).filter(last_name=post.last_name)[0].sap_id
			post.laptop_access = True
			post.terminal_access = False			
			post.save()
			print(post.sap_id)
            		#return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'philipp_app/user_edit.html', {'form': form})

