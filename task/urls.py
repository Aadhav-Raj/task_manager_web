from django.urls import path
from . import views
from . import api_views
from . import serializers
urlpatterns=[
    path("add/",views.add,name="addTask"),
    path("list/",views.list,name="list"),
    path("api/list/",api_views.ListTasks,name="List_Tasks"),
    path("api/list2/",api_views.ListTasks2,name="List_Tasks2"),
    path("api/add/",api_views.AddTask,name="Add_Task"),#http://192.168.137.1:8000/api/add/?head=Buy Groseries &desc=buy for a week
    path("api/delete/<int:pk>",views.Detele.as_view(),name="Delete_Task"),
    path("api/complete/<int:pk>",api_views.complete,name="Completed Task"),
    path("api/signup/",api_views.createUser,name="api_signup"),
    path('api/login/', api_views.user_login, name='api_login'),
    path('api/logout/', api_views.user_logout, name='api_logout'),
    path('api/profile/', api_views.user_profile, name='api_profile'),
    path('api/authentication/',api_views.verify_email,name="verify_email"),
    path('api/verify/',api_views.verify_otp,name="verify_email"),
    path("api/hello/",views.HelloView.as_view(),name="hello"),
    path("dashboard/",views.admin,name="admin"),
    path('login/', views.user_login, name='login'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('logout/', views.user_logout, name='logout'),
]