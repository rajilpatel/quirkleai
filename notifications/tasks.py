# Placeholder for background notification tasks
from apscheduler.schedulers.background import BackgroundScheduler
from reminders.tasks import send_session_reminders

scheduler = BackgroundScheduler()

scheduler.add_job(send_session_reminders, 'interval', minutes=30)

scheduler.start()
