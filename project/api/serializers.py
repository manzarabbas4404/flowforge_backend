from rest_framework import serializers
from project.models import Project, Task


class ProjectSerializer(serializers.ModelSerializer):
    organization = serializers.CharField(source="organization.name", read_only=True)

    class Meta:
        model = Project
        fields = (
            "id",
            "name",
            "description",
            "organization",
            "is_archived",
            "created_at",
            "updated_at",
        )


class TaskSerializer(serializers.ModelSerializer):
    project = serializers.CharField(source="project.name", read_only=True)
    organization = serializers.CharField(
        source="project.organization.name", read_only=True
    )
    assigned_to = serializers.CharField(source="assigned_to.username", read_only=True)

    class Meta:
        model = Task
        fields = (
            "id",
            "title",
            "description",
            "status",
            "priority",
            "project",
            "project",
            "organization",
            "assigned_to",
            "assigned_to",
            "due_date",
            "is_deleted",
            "created_at",
            "updated_at",
        )
