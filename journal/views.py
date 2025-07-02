from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.db import IntegrityError
import traceback

from .models import JournalEntry, RecapPreference, ReflectionSummary
from .serializers import (
    JournalEntrySerializer,
    RecapPreferenceSerializer,
    ReflectionSummarySerializer,
)
from .forms import JournalEntryForm  # You need to create this form if it doesn't exist


class JournalEntryHTMXFormView(LoginRequiredMixin, View):
    def get(self, request):
        print(
            f"[DEBUG] GET request received - User: {request.user}, HTMX: {request.headers.get('HX-Request')}"
        )

        # Check if this is an HTMX request (for the form partial)
        if request.headers.get("HX-Request"):
            print("[DEBUG] HTMX GET request - returning form partial")
            form = JournalEntryForm()
            return render(
                request, "journal/partials/journalentry_form.html", {"form": form}
            )

        # Regular page request - render the full page
        print("[DEBUG] Regular GET request - returning full page")
        return render(request, "journal/journal_entry_page.html")

    def post(self, request):
        print(f"[DEBUG] POST request received - User: {request.user}")
        print(f"[DEBUG] POST data: {request.POST}")
        print(f"[DEBUG] FILES: {request.FILES}")

        # Check if this is a replacement request
        if request.POST.get("replace_existing"):
            print("[DEBUG] Replacement request detected")
            return self.handle_replacement(request)

        form = JournalEntryForm(request.POST, request.FILES)
        print(f"[DEBUG] Form is valid: {form.is_valid()}")

        if form.is_valid():
            print("[DEBUG] Form is valid, attempting to save...")
            print(f"[DEBUG] Form cleaned data: {form.cleaned_data}")

            # Check for existing entry BEFORE trying to save
            existing_entry = JournalEntry.objects.filter(
                user=request.user,
                date=form.cleaned_data["date"],
                entry_type=form.cleaned_data["entry_type"],
            ).first()

            print(f"[DEBUG] Existing entry check: {existing_entry}")

            if existing_entry:
                print("[DEBUG] Duplicate detected - returning confirmation modal")
                return render(
                    request,
                    "journal/partials/duplicate_confirmation_modal.html",
                    {
                        "form": form,
                        "existing_entry": existing_entry,
                        "new_data": form.cleaned_data,
                    },
                )

            # No duplicate, proceed with save
            try:
                entry = form.save(commit=False)
                entry.user = request.user
                print(f"[DEBUG] About to save entry: {entry}")
                entry.save()
                print(f"[DEBUG] Entry saved successfully with ID: {entry.id}")

                # Return a partial or success message for HTMX
                return render(
                    request,
                    "journal/partials/journalentry_success.html",
                    {"entry": entry},
                )
            except IntegrityError as e:
                print(f"[DEBUG] IntegrityError caught during save: {e}")
                print(f"[DEBUG] Error details: {traceback.format_exc()}")
                form.add_error(None, "An error occurred while saving the entry.")
                return render(
                    request, "journal/partials/journalentry_form.html", {"form": form}
                )
        else:
            print(f"[DEBUG] Form errors: {form.errors}")
            return render(
                request, "journal/partials/journalentry_form.html", {"form": form}
            )

    def handle_replacement(self, request):
        """Handle replacement of existing entry"""
        print("[DEBUG] Handling replacement request")

        try:
            existing_entry_id = request.POST.get("existing_entry_id")
            content = request.POST.get("content")
            irl_mode = request.POST.get("irl_mode") == "true"

            print(
                f"[DEBUG] Replacement data - ID: {existing_entry_id}, Content: {content}, IRL: {irl_mode}"
            )

            # Get the existing entry
            existing_entry = JournalEntry.objects.get(
                id=existing_entry_id, user=request.user
            )
            print(f"[DEBUG] Found existing entry: {existing_entry}")

            # Update the existing entry
            existing_entry.content = content
            existing_entry.irl_mode = irl_mode

            # Handle file upload if present
            if request.FILES.get("media"):
                existing_entry.media = request.FILES["media"]

            existing_entry.save()
            print(f"[DEBUG] Entry updated successfully")

            return render(
                request,
                "journal/partials/journalentry_success.html",
                {"entry": existing_entry},
            )
        except Exception as e:
            print(f"[DEBUG] Error in replacement: {e}")
            print(f"[DEBUG] Error details: {traceback.format_exc()}")
            return JsonResponse({"error": str(e)}, status=400)


class JournalEntryViewSet(viewsets.ModelViewSet):
    serializer_class = JournalEntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return JournalEntry.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RecapPreferenceViewSet(viewsets.ModelViewSet):
    serializer_class = RecapPreferenceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return RecapPreference.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ReflectionSummaryViewSet(viewsets.ModelViewSet):
    serializer_class = ReflectionSummarySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ReflectionSummary.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# Create your views here.
