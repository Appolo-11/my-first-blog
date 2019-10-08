from django.shortcuts import render

def access_table_list(request):
    return render(request, 'philipp_app/access_table_list.html', {})
