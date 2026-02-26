from rest_framework import generics, viewsets, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend

from .models import Task
from .serializers import TaskSerializer, RegisterSerializer
from .permissions import IsOwner


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = []


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsOwner]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = ["status", "due_date", "priority"]
    search_fields = ["title", "description"]
    ordering_fields = ["due_date", "created_at", "priority"]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    @action(detail=True, methods=["patch"])
    def complete(self, request, pk=None):
        task = self.get_object()
        task.status = Task.StatusChoices.COMPLETED
        task.save()
        return Response({"message": "Task marked as completed"})

    @action(detail=True, methods=["patch"])
    def incomplete(self, request, pk=None):
        task = self.get_object()
        task.status = Task.StatusChoices.PENDING
        task.save()
        return Response({"message": "Task marked as pending"})