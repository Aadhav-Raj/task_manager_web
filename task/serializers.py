from rest_framework import serializers
from .models import Task
from rest_framework import generics

class TaskSerializer(serializers.Serializer):
    #id:serializers.CharField()
    head=serializers.CharField()
    desc=serializers.CharField()

class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields="__all__"
class TaskAddSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields=[

            "head","desc"]


class TaskDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields="__all__"