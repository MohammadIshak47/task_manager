
from rest_framework import serializers
from tasks.models import Task, TaskPhoto

class TaskPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskPhoto
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    photos = TaskPhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = '__all__'
