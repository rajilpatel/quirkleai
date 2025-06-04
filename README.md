# QuirkleAI Platform

This repository contains a minimal Django & React codebase intended as a starting point for a teletherapy platform. It exposes REST endpoints for sessions, notes, transcripts, users and notifications. While simplified, the project structure mirrors that of a production application so investors and mental health professionals can evaluate the concept.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run migrations and start the server:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

## Apps

- **users** – custom user model with therapist/client roles
- **sessions** – schedule therapy sessions
- **notes** – record session notes (SOAP, DAP or freeform)
- **transcripts** – upload audio transcripts
- **notifications** – simple notification system

The frontend folder includes React components such as a calendar and notes editor. These are placeholders and can be expanded into a fully interactive interface.

This project is intentionally lightweight but provides a structure that can be built upon for an investment‑ready platform.
