from rest_framework.serializers import ModelSerializer
from .models import Tasks

class TasksSerializer(ModelSerializer):

    class Meta:
        model = Tasks
        # Los datos que seran mostrados
        fields = ['title','description','status','priority','created_at','updated_at']
        # Los datos que seran mostrados pero no requieren ser ingresados en un POST
        read_only_fields = ['created_at','updated_at']