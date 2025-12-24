# Here are the Admin Register 
# For testing added one more line
from django.contrib import admin
from project.models import Project, Task
from django.db.models import Prefetch


# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "organization",
        "is_archived",
        "created_at",
        "updated_at",
    )


class TaskAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.select_related(
            "project", "project__organization", "assigned_to"
        ).prefetch_related(
            Prefetch(
                "project__organization__organizationmember_set", to_attr="members_list"
            )
        )
        return qs

    list_display = (
        "title",
        "project_name",
        "organization_name",
        "assigned_user",
        "assigned_user_role",
        "status",
        "priority",
        "due_date",
        "is_deleted",
    )

    # ---------- Helper methods ----------
    def project_name(self, obj):
        return obj.project.name

    project_name.short_description = "Project"

    def organization_name(self, obj):
        return obj.project.organization.name

    organization_name.short_description = "Organization"

    def assigned_user(self, obj):
        return obj.assigned_to.username if obj.assigned_to else "-"

    assigned_user.short_description = "User"

    def assigned_user_role(self, obj):
        # Get role from OrganizationMember
        member = next(
            (
                m
                for m in obj.project.organization.members_list
                if m.user_id == obj.assigned_to_id
            ),
            None,
        )

        return member.role if member else "-"

    assigned_user_role.short_description = "Role"


admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
