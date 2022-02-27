from django.shortcuts import render

def index(request):
    return render(request, 'logic_tasks/logic_tasks.html')