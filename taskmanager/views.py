from django.shortcuts import render

# Create your views here.
def get_tasks(request):
    return render(request, "taskmanager/tasks.html")