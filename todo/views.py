from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task
from django.utils import timezone

class TaskListView(ListView):
    model = Task
    template_name = 'todo/task_list.html'
    context_object_name = 'tasks'

class CompletedTaskListView(ListView):
    model = Task
    template_name = 'todo/completed_tasks.html'
    context_object_name = 'completed_tasks'
    queryset = Task.objects.filter(completed=True)

class MyDayTaskListView(ListView):
    model = Task
    template_name = 'todo/my_day_tasks.html'
    context_object_name = 'my_day_tasks'
    queryset = Task.objects.filter(due_date=timezone.now().date())

class TaskCreateView(CreateView):
    model = Task
    template_name = 'todo/task_create.html'
    fields = ['title', 'important', 'due_date']
    success_url = reverse_lazy('todo:task_list')

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'todo/task_update.html'
    fields = ['title', 'important', 'completed', 'due_date']
    success_url = reverse_lazy('todo:task_list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'todo/task_delete.html'
    success_url = reverse_lazy('todo:task_list')
