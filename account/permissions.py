from rest_framework.permissions import BasePermission
from organization.models import OrganizationMember


class IsOrgMember(BasePermission):
    """
    Permission: User must belong to the organization.
    Works for both class-level and object-level checks.
    """

    def has_permission(self, request, view):
        # For list/create: user must belong to at least one organization
        user = request.user
        return OrganizationMember.objects.filter(user=user).exists()

    def has_object_permission(self, request, view, obj):
        # For retrieve/update/delete: user must belong to object's organization
        user = request.user
        return OrganizationMember.objects.filter(
            user=user, organization=obj.organization
        ).exists()


class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        # block anonymous users
        if not request.user or not request.user.is_authenticated:
            return False
        return True

    def has_object_permission(self, request, view, obj):
        member = OrganizationMember.objects.filter(
            user=request.user, organization=obj.project.organization
        ).first()
        return member and member.role in ["admin", "owner"]


class IsOwner(BasePermission):
    """
    Permission: user must be owner of the organization.
    """

    def has_object_permission(self, request, view, obj):
        user = request.user
        member = OrganizationMember.objects.filter(
            user=user, organization=obj.organization
        ).first()
        return member and member.role == "owner"
