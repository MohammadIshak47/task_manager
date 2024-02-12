from django.urls import path 
from .views import TaskListView, TaskCreateView, TaskDetailView, TaskUpdateView, TaskDeleteView,signup

urlpatterns = [
    path('', TaskListView.as_view(), name='task-list'),
    path('accounts/registration/',signup,name='signup'),
    path('create/', TaskCreateView.as_view(), name='task-create'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
]
