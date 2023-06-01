from django.urls import path
from todo.views import TaskListView, CompletedTaskListView, MyDayTaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView

app_name = 'todo'

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('completed/', CompletedTaskListView.as_view(), name='completed_tasks'),
    path('myday/', MyDayTaskListView.as_view(), name='my_day_tasks'),
    path('task/create/', TaskCreateView.as_view(), name='task_create'),
    path('task/update/<int:pk>/', TaskUpdateView.as_view(), name='task_update'),
    path('task/delete/<int:pk>/', TaskDeleteView.as_view(), name='task_delete'),
]
