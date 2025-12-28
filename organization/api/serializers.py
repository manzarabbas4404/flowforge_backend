from rest_framework import serializers
from organization.models import Organization, OrganizationMember
from account.api.serializers import UserSerializer


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = (
            "id",
            "name",
            "slug",
            "created_at",
            "updated_at",
        )


class OrganizationMemberSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = OrganizationMember
        fields = (
            "id",
            "user",
            "organization",
            "role",
            "joined_at",
        )
