from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Task(models.Model):

    class PriorityChoices(models.TextChoices):
        LOW = "LOW", "Low"
        MEDIUM = "MEDIUM", "Medium"
        HIGH = "HIGH", "High"

    class StatusChoices(models.TextChoices):
        PENDING = "PENDING", "Pending"
        COMPLETED = "COMPLETED", "Completed"

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="tasks"
    )

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    due_date = models.DateField()
    priority = models.CharField(
        max_length=10,
        choices=PriorityChoices.choices,
        default=PriorityChoices.MEDIUM
    )

    status = models.CharField(
        max_length=10,
        choices=StatusChoices.choices,
        default=StatusChoices.PENDING
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["user"]),
            models.Index(fields=["status"]),
            models.Index(fields=["due_date"]),
        ]

    def __str__(self):
        return f"{self.title} ({self.user.username})"

    def is_overdue(self):
        return self.due_date < timezone.now().date() and self.status != self.StatusChoices.COMPLETED