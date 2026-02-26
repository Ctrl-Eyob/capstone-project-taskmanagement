from rest_framework import serializers
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Task


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class TaskSerializer(serializers.ModelSerializer):
    is_overdue = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = ["user", "created_at", "updated_at"]

    def get_is_overdue(self, obj):
        return obj.is_overdue()

    def validate_due_date(self, value):
        if value < timezone.now().date():
            raise serializers.ValidationError("Due date cannot be in the past.")
        return value

    def create(self, validated_data):
        return Task.objects.create(
            user=self.context["request"].user,
            **validated_data
        )