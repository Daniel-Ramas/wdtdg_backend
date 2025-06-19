from rest_framework import serializers
from .models import JournalEntry, RecapPreference, ReflectionSummary


class JournalEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = JournalEntry
        fields = [
            "id",
            "user",
            "date",
            "entry_type",
            "content",
            "media",
            "irl_mode",
            "created_at",
        ]
        read_only_fields = ["user", "created_at"]


class RecapPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecapPreference
        fields = ["user", "frequency"]


class ReflectionSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = ReflectionSummary
        fields = [
            "id",
            "user",
            "period_start",
            "period_end",
            "summary_text",
            "share_link",
            "is_public",
            "created_at",
        ]
        read_only_fields = ["user", "share_link", "created_at"]
