from django.db import models
from organization.models import Organization
from project.model_managers import ActiveProjectManager
from django.contrib.auth import get_user_model

User = get_user_model()


class Project(models.Model):

    objects = models.Manager()
    active_projects = ActiveProjectManager()

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, related_name="projects"
    )
    is_archived = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [models.Index(fields=["organization", "is_archived"])]
        verbose_name = "Project"
        constraints = [
            models.UniqueConstraint(
                fields=["organization", "name"], name="unique_project_per_organization"
            )
        ]

    def __str__(self):
        return f"{self.name} ({self.organization.name})"


class Task(models.Model):

    STATUS_CHOICES = (
        ("TODO", "To Do"),
        ("IN_PROGRESS", "In Progress"),
        ("DONE", "Done"),
        ("BLOCKED", "Blocked"),
    )

    PRIORITY_CHOICES = (
        ("LOW", "Low"),
        ("MEDIUM", "Medium"),
        ("HIGH", "High"),
        ("CRITICAL", "Critical"),
    )

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="TODO")
    priority = models.CharField(
        max_length=20, choices=PRIORITY_CHOICES, default="MEDIUM"
    )
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="project"
    )
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="Assigned_to",
    )
    due_date = models.DateField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)  # soft delete
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [models.Index(fields=["status", "assigned_to", "due_date"])]
        verbose_name = "Task"
        ordering = ["due_date", "priority"]

    def __str__(self):
        return f"{self.title} ({self.project.name})"
