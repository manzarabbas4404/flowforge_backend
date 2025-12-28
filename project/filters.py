from project.models import Project
from django_filters import rest_framework as filters


class ProjectFilter(filters.FilterSet):
    organization = filters.CharFilter(field_name="organization__name")

    class Meta:
        model = Project
        fields = ["organization", "is_archived"]
