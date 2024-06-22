from django.urls import path
from .views import TasksListAPIView, TaskInfoAPIView, CreateTaskAPIView, UpdateTaskAPIView, DeleteTaskAPIView

urlpatterns = [
    path('tasks/', TasksListAPIView.as_view(), name='tasks'),
    path('tasks/<int:task_id>/info/', TaskInfoAPIView.as_view(), name='task_info'),
    path('tasks/create/', CreateTaskAPIView.as_view(), name='create_task'),
    path('tasks/<int:pk>/update/', UpdateTaskAPIView.as_view(), name='update_task'),
    path('tasks/<int:pk>/delete/', DeleteTaskAPIView.as_view(), name='delete_task'),
]