from django.shortcuts import render
from django.http import HttpResponse
from todo_list_app.models import *
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def home(request):
     return render(request, 'todo_list_app/home.html')

def signup(request):
     return render(request, 'todo_list_app/signup.html')

@csrf_exempt
def mylist(request):
    if request.method == "POST":
    	date = request.POST.get('due_date') 
    	print date
        print request.POST.get('title')
        title = request.POST.get('title')
        desc = request.POST.get('description')
        priority = request.POST.get('priorities')
        status = "Todo"
    	new_task = Task(name = title ,description = desc ,priorities = priority ,status = status ,due_date = date)
    	new_task.save()
    return render(request, 'todo_list_app/mylist.html')

def tasks(request):
	current_date = datetime.now()
    tasks = Task.objects.all()
    return render(request, 'todo_list_app/task.html' ,{'tasks':tasks} ,{'current_date':current_date})