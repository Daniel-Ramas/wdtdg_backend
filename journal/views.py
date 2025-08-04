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
