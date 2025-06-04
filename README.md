# QuirkleAI

This repository is a simple skeleton for a therapy management application built with Django and Django REST Framework. It includes the following apps:

- **users** – custom user model with roles and authentication endpoints.
- **sessions** – manages therapy sessions including a simple Jitsi room name generator.
- **notes** – allows therapists to create SOAP/DAP/freeform notes for sessions.
- **transcripts** – stores audio transcripts and provides a dummy processing endpoint.
- **notifications** – basic notifications model with a background scheduler.
- **reminders** – task for emailing upcoming session reminders.

## Getting Started

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Apply migrations and create a superuser:

```bash
python manage.py migrate
python manage.py createsuperuser
```

3. Run the development server:

```bash
python manage.py runserver
```

API endpoints are available under `/api/`.
