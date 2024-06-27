from django.urls import path
from . import views
from . import api_views
from . import serializers
urlpatterns=[
    path("add/",views.add,name="addTask"),
    path("list/",views.list,name="list"),
    path("api/list/",api_views.ListTasks,name="List_Tasks"),
    path("api/add/",api_views.AddTask,name="Add_Task"),#http://192.168.137.1:8000/api/add/?head=Buy Groseries &desc=buy for a week
    path("api/delete/<int:pk>",views.Detele.as_view(),name="Delete_Task")
]