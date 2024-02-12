from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from tasks.models import Task
from tasks.forms import TaskCreateForm,TaskUpdateForm
from django.db.models import Q


class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    ordering = ['-created_at']  # Sort tasks by creation date by default
    def get_queryset(self):
        queryset = super().get_queryset()
        task_status = self.request.GET.get('task_status')
        
        # Filter queryset based on task_status
        if task_status:
            queryset = queryset.filter(task_status=task_status)
            
        search_query = self.request.GET.get('search')
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(description__icontains=search_query)
            )
        return queryset 

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskCreateForm
    template_name = 'tasks/task_create.html'
    success_url = reverse_lazy('task-list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task_details.html'
    context_object_name = 'task_detail'

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskUpdateForm
    template_name = 'tasks/task_update.html'
    success_url = reverse_lazy('task-list')
    

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task_delete.html'
    context_object_name = 'task_delete'
    success_url = reverse_lazy('task-list')





