from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from tasks.models import Task
from tasks.forms import TaskCreateForm


class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    ordering = ['-created_at']  # Sort tasks by creation date by default

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskCreateForm
    template_name = 'tasks/task_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task_details.html'

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'tasks/task_update.html'
    fields = ['title', 'description', 'due_date', 'priority']

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task_delete.html'
    success_url = reverse_lazy('task-list')





