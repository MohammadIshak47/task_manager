from django.contrib import admin
from .models import Task, TaskPhoto

class TaskPhotoInline(admin.TabularInline):
    model = TaskPhoto

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date', 'priority', 'is_complete', 'created_at', 'updated_at')
    list_filter = ('priority', 'is_complete')
    search_fields = ('title',)
    inlines = [
        TaskPhotoInline,
    ]

@admin.register(TaskPhoto)
class TaskPhotoAdmin(admin.ModelAdmin):
    list_display = ('task', 'photo')

