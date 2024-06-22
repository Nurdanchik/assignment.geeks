from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Task
from .serializers import TaskSerializer

class TasksListAPIView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskInfoAPIView(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        task_id = self.kwargs['task_id']
        return Task.objects.filter(id=task_id)
    
class CreateTaskAPIView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class DeleteTaskAPIView(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class UpdateTaskAPIView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer