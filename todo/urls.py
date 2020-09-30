from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasks_list, name='tasks_list'),
    path('task_edit/<int:pk>/', views.edit_task, name='edit_task'),
    path('task_delete/<int:pk>/', views.delete_task, name='delete_task'),
]
