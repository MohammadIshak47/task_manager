from django.shortcuts import render,redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from tasks.models import Task
from tasks.forms import TaskCreateForm,TaskUpdateForm,NewUserForm
from django.db.models import Q
from django.contrib.auth import login

class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    ordering = ['-created_at']  # Sort tasks by creation date by default
    
    def get_queryset(self):
        queryset = super().get_queryset()

        # Search by title
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(title__icontains=search_query)

        # Filter by creation date
        creation_date_filter = self.request.GET.get('creation_date', '')
        if creation_date_filter:
            queryset = queryset.filter(created_at=creation_date_filter)

        # Filter by due date
        due_date_filter = self.request.GET.get('due_date', '')
        if due_date_filter:
            queryset = queryset.filter(due_date=due_date_filter)

        # Filter by priority
        priority_filter = self.request.GET.get('priority', '')
        if priority_filter:
            queryset = queryset.filter(priority=priority_filter)

        # Filter by completion status
        is_complete_filter = self.request.GET.get('is_complete', '')
        if is_complete_filter in ['True', 'False']:
            is_complete_bool = is_complete_filter == 'True'
            queryset = queryset.filter(is_complete=is_complete_bool)

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


def signup(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/')
    
    return render(request,'registration/signup.html',{'form':form})



