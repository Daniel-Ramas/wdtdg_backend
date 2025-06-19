from django.urls import path
from .views import JournalEntryHTMXFormView

urlpatterns = [
    path(
        "htmx/journal-entry-form/",
        JournalEntryHTMXFormView.as_view(),
        name="journalentry_htmx_form",
    ),
]
