from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend

from .models import Task
from .serializers import TaskSerializer, RegisterSerializer
from .permissions import IsOwner


# User Registration
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = []


# Task ViewSet (CRUD)
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsOwner]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["status", "due_date"]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    @action(detail=True, methods=["patch"])
    def complete(self, request, pk=None):
        task = self.get_object()
        task.status = True
        task.save()
        return Response({"message": "Task marked as complete"})

    @action(detail=True, methods=["patch"])
    def incomplete(self, request, pk=None):
        task = self.get_object()
        task.status = False
        task.save()
        return Response({"message": "Task marked as incomplete"})