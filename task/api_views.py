from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .forms import AddTaskForm
from . import serializers
@api_view(['GET'])
def ListTasks(request):
    """task=Task.objects.all()
    id=Task.objects.filter()
    task_serializer=TaskSerializer(task,many=True)
    return Response(task_serializer.data)"""

    task=Task.objects.all()
    task_serializer=serializers.TaskListSerializer(task,many=True)
    return Response(task_serializer.data)

@api_view(['POST'])
def AddTask(request):
    #task_head=request.POST.get('head')
    #task_desc=request.POST.get('desc')
    #task=Task(head="",desc="")
    #if  not  task_desc or  not task_desc:
     #   return Response({'error': 'Head and description are required. {}'.format()}, status=status.HTTP_400_BAD_REQUEST)


    #task={"head":task_head,"desc":task_desc}
    serializer=serializers.TaskAddSerializer(data=request.data)


    if serializer.is_valid():
        task=serializer.save()
        return Response({"id":task.id},status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#@api_view([''])

