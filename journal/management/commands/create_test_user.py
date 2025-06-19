from django.core.management.base import BaseCommand
from django.conf import settings
from wdtdg_backend.users.models import User
from rest_framework.authtoken.models import Token


class Command(BaseCommand):
    help = "Creates a test user and token for local development"

    def handle(self, *args, **options):
        if not settings.DEBUG:
            self.stdout.write(
                self.style.ERROR("This command can only be run in DEBUG mode")
            )
            return

        email = settings.TEST_USER_EMAIL
        password = settings.TEST_USER_PASSWORD

        user, created = User.objects.get_or_create(
            email=email,
            defaults={"name": "Test User", "is_staff": True, "is_superuser": True},
        )

        if created:
            user.set_password(password)
            user.save()
            self.stdout.write(self.style.SUCCESS(f"Created test user: {email}"))
        else:
            self.stdout.write(self.style.WARNING(f"Test user {email} already exists"))

        # Create or get token
        token, created = Token.objects.get_or_create(user=user)
        if created:
            self.stdout.write(self.style.SUCCESS(f"Created token for {email}"))
        else:
            self.stdout.write(self.style.WARNING(f"Token for {email} already exists"))

        self.stdout.write(self.style.SUCCESS(f"Token: {token.key}"))
