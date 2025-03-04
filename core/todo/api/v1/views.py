from rest_framework import viewsets
from .serializers import TaskSerializer
from ...models import Task
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    filter_backends = [OrderingFilter]

    ordering_fields = ["created_date"]
