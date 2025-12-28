from django.shortcuts import render
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
    UpdateModelMixin,
)
from rest_framework.viewsets import GenericViewSet
from account.api.serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.pagination import PageNumberPagination
from account.permissions import IsOrgMember, IsAdmin, IsOwner

# from account.customauth import UserCustomAuthentication
# from rest_framework.authentication import BasicAuthentication, SessionAuthentication
# from rest_framework.permissions import IsAuthenticatedOrReadOnly

User = get_user_model()


class UserViewSet(
    GenericViewSet,
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination
    # authentication_classes = [UserCustomAuthentication]
    permission_classes = [IsAdmin]
