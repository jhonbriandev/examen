from rest_framework import viewsets
from .models import Tasks
from .serializers import TasksSerializer
from rest_framework.permissions import  IsAuthenticatedOrReadOnly

class TasksViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

