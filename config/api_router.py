from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter
from wdtdg_backend.users.api.views import UserViewSet
from journal.views import (
    JournalEntryViewSet,
    RecapPreferenceViewSet,
    ReflectionSummaryViewSet,
)

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("users", UserViewSet)
router.register("journal-entries", JournalEntryViewSet, basename="journal-entry")
router.register(
    "recap-preferences", RecapPreferenceViewSet, basename="recap-preference"
)
router.register(
    "reflection-summaries", ReflectionSummaryViewSet, basename="reflection-summary"
)

app_name = "api"
urlpatterns = router.urls
