from django.shortcuts import render
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
    UpdateModelMixin,
)
from rest_framework.viewsets import GenericViewSet
from project.models import Project, Task
from project.api.serializers import ProjectSerializer, TaskSerializer
from project.filters import ProjectFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import PageNumberPagination

# from account.customauth import UserCustomAuthentication
# from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated


class ProjectViewSet(
    GenericViewSet,
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    # filter_backends = [DjangoFilterBackend]
    filterset_class = ProjectFilter
    pagination_class = PageNumberPagination
    # filterset_fields = ['name']
    # authentication_classes = [UserCustomAuthentication]
    # permission_classes = [IsAuthenticatedOrReadOnly]


class TaskViewSet(
    GenericViewSet,
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # permission_classes = [IsAuthenticated]
    filterset_fields = ["title", "description"]
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ["id"]
    search_fields = ["title"]
    pagination_class = PageNumberPagination
    # authentication_classes = [UserCustomAuthentication]
