from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

app_name="polls"

router = DefaultRouter()
router.register("", views.PollsViewSet)


urlpatterns = router.urls