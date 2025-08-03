from django.urls import path
from .views import JournalEntryHTMXFormView, JournalEntryListView, JournalEntryEditView

urlpatterns = [
    path(
        "htmx/journal-entry-form/",
        JournalEntryHTMXFormView.as_view(),
        name="journalentry_htmx_form",
    ),
    path(
        "",
        JournalEntryListView.as_view(),
        name="journal_entry_list",
    ),
    path(
        "edit/<uuid:pk>/",
        JournalEntryEditView.as_view(),
        name="journal_entry_edit",
    ),
]
