from django.shortcuts import render
from .models import Task
from .forms import AddTaskForm
from task_manager import urls
from rest_framework import generics
from django.urls import get_resolver
# Create your views here.
from .serializers import *
def add(request):
    if request.method=="POST":
        form=AddTaskForm(request.POST)
        if form.is_valid() and form.cleaned_data:
            task=form.save()

    else:
       form = AddTaskForm()
    return render(request,"addTask.html",{"form":form})


def list(request):
    tasks = Task.objects.all()
    return render(request,"listTask.html",{"tasks":tasks})

def home(request):
    return render(request,"home.html",{"urls":urls.urlpatterns})

class Detele(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDeleteSerializer


