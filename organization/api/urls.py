from rest_framework.routers import DefaultRouter
from organization.api.views import (
    OrganizationViewSet,
    OrganizationMemberViewSet,
)

router = DefaultRouter()
router.register("organizations", OrganizationViewSet, basename="organizations")
router.register(
    "organization-members", OrganizationMemberViewSet, basename="organization-members"
)

urlpatterns = router.urls
