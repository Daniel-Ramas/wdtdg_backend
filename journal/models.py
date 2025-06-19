import uuid
from django.db import models

from wdtdg_backend.users.models import User


# Create your models here.
class JournalEntry(models.Model):
    TEXT = "text"
    VOICE = "voice"
    PHOTO = "photo"
    VIDEO = "video"

    ENTRY_TYPES = [
        (TEXT, "Text"),
        (VOICE, "Voice"),
        (PHOTO, "Photo"),
        (VIDEO, "Video"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="entries")
    date = models.DateField()
    entry_type = models.CharField(max_length=10, choices=ENTRY_TYPES)
    content = models.TextField(blank=True, null=True)
    media = models.FileField(upload_to="entries/media/", blank=True, null=True)
    irl_mode = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        unique_together = ("user", "date", "entry_type")


class RecapPreference(models.Model):
    WEEKLY = "weekly"
    BIWEEKLY = "biweekly"
    MONTHLY = "monthly"
    QUARTERLY = "quarterly"
    BIANNUALLY = "biannually"
    ANNUALLY = "annually"

    FREQUENCY_CHOICES = [
        (WEEKLY, "Weekly"),
        (BIWEEKLY, "Biweekly"),
        (MONTHLY, "Monthly"),
        (QUARTERLY, "Quarterly"),
        (BIANNUALLY, "Biannually"),
        (ANNUALLY, "Annually"),
    ]

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="recap_pref"
    )
    frequency = models.CharField(
        max_length=20, choices=FREQUENCY_CHOICES, default=MONTHLY
    )


class ReflectionSummary(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="summaries")
    period_start = models.DateField()
    period_end = models.DateField()
    summary_text = models.TextField()
    share_link = models.CharField(max_length=32, unique=True)
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
