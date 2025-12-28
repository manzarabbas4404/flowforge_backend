from rest_framework.routers import DefaultRouter
from account.api.views import UserViewSet

router = DefaultRouter()
router.register("user", UserViewSet, basename="user")

urlpatterns = router.urls
