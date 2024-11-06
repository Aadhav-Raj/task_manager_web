from django.shortcuts import render,redirect
from .models import Task
from .forms import AddTaskForm,SignupForm,LoginForm
from task_manager import urls
from django.contrib import auth
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from rest_framework import generics
from django.urls import get_resolver, reverse_lazy
# Create your views here.
from .serializers import *
def add(request):
    if request.method=="POST":
        form=AddTaskForm(request.POST,user=request.user)

        if form.is_valid() and form.cleaned_data:
            #form["user"]=auth.get_user(request)
            form.fields["user"].initial=auth.get_user(request)
            #["user"]=auth.get_user(request)
            task=form.save()

    else:
       form = AddTaskForm(user=request.user)
    return render(request,"addTask.html",{"form":form})


def list(request):
    tasks = Task.objects.filter(user=request.user.pk)
    return render(request,"listTask.html",{"tasks":tasks})

def home(request):
    return render(request,"home.html",{"urls":urls.urlpatterns})

class Detele(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDeleteSerializer

class Update(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCompletionSerializer

def admin(request):
    task=Task.objects.all()
    return  render(request,"admin.html",{"objects":task})


def user_signup(request):
    if request.method == "POST":
        print("qwertg")
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print(form.errors)
    else:
        print("zxcvbnm")
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('list')
            else:
                return render(request, 'login.html', {'form': form, 'error': 'Invalid email or password'})
        else:
            print(form.errors)
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    auth_logout(request)
    return redirect('login')



from django.views.generic import *
from .forms import SignupForm

class SignUpView(CreateView):
     form_class = SignupForm
     success_url = reverse_lazy('login')
     template_name = 'signup.html'


from rest_framework.views import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class HelloView(APIView):
    #permission_classes = IsAuthenticated
    def get(self,request):

        content={"message : Hello "+str(request.user.username)}
        return Response(content)

from django.views.generic import CreateView
"""
def user_signup(request):
    if request.method=="POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            user=form.save()
            return redirect('login')
    else:
        form=SignupForm()
    return render(request,'signup.html',{'form':form})

"""
"""
class user_signup(CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user:
                auth_login(request, user)
                return redirect("list")
            else:
                return render(request, "login.html", {"form": form, "error": "Invalid email or password"})
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})

def user_logout(request):
    logout(request)
    return redirect("login")

"""
