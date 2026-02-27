from rest_framework import generics, viewsets, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from django.core.mail import send_mail
from django.conf import settings

from .models import Task, Category, Profile
from .serializers import (
    TaskSerializer,
    RegisterSerializer,
    CategorySerializer,
    ProfileSerializer
)
from .permissions import IsOwner


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = []


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsOwner]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = ["status", "due_date", "priority", "category"]
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

    @action(detail=True, methods=["post"])
    def send_reminder(self, request, pk=None):
        task = self.get_object()

        if not task.user.profile.email_notifications:
            return Response({"message": "Email notifications disabled"})

        send_mail(
            subject=f"Reminder: {task.title}",
            message=f"Your task '{task.title}' is due on {task.due_date}.",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[task.user.email],
        )

        return Response({"message": "Reminder email sent"})


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)