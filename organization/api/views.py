from django.shortcuts import render
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
    UpdateModelMixin,
)
from rest_framework.viewsets import GenericViewSet
from organization.api.serializers import (
    OrganizationSerializer,
    OrganizationMemberSerializer,
)
from django.contrib.auth import get_user_model
from organization.models import Organization, OrganizationMember
from rest_framework.pagination import PageNumberPagination

# from account.customauth import UserCustomAuthentication
# from rest_framework.authentication import BasicAuthentication, SessionAuthentication
# from rest_framework.permissions import IsAuthenticatedOrReadOnly

User = get_user_model()


class OrganizationViewSet(
    GenericViewSet,
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    pagination_class = PageNumberPagination
    # authentication_classes = [UserCustomAuthentication]
    # permission_classes = [IsAuthenticatedOrReadOnly]


class OrganizationMemberViewSet(
    GenericViewSet,
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
):
    queryset = OrganizationMember.objects.all()
    serializer_class = OrganizationMemberSerializer
    pagination_class = PageNumberPagination
    # authentication_classes = [UserCustomAuthentication]
    # permission_classes = [IsAuthenticatedOrReadOnly]
