from datetime import timedelta
from django.utils import timezone
from django.core.mail import send_mail

from sessions.models import TherapySession


def send_session_reminders():
    upcoming = TherapySession.objects.filter(scheduled_for__lte=timezone.now() + timedelta(hours=1))
    for session in upcoming:
        send_mail(
            'Session Reminder',
            f'You have a session at {session.scheduled_for}',
            'noreply@example.com',
            [session.client.email],
            fail_silently=True,
        )
