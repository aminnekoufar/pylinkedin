from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from pylinkedin.users.api.views import UserEducationViewSet, UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("user-educations", UserEducationViewSet, basename="educations")
app_name = "api"
urlpatterns = router.urls
