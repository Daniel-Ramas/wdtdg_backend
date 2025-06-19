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
from django.http import HttpResponse
from django.views import View

from .models import JournalEntry, RecapPreference, ReflectionSummary
from .serializers import (
    JournalEntrySerializer,
    RecapPreferenceSerializer,
    ReflectionSummarySerializer,
)
from .forms import JournalEntryForm  # You need to create this form if it doesn't exist


class JournalEntryHTMXFormView(LoginRequiredMixin, View):
    def get(self, request):
        form = JournalEntryForm()
        return render(
            request, "journal/partials/journalentry_form.html", {"form": form}
        )

    def post(self, request):
        form = JournalEntryForm(request.POST, request.FILES)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            # Return a partial or success message for HTMX
            return render(
                request, "journal/partials/journalentry_success.html", {"entry": entry}
            )
        return render(
            request, "journal/partials/journalentry_form.html", {"form": form}
        )


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
