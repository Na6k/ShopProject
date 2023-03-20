from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def get_letter(name, email, subject, company, message):
    letter = send_mail(
        f"{name}: {subject}",
        f"Вам пишет {name} из {company}, по теме: {subject},\n\
              сообщение: {message}, обратная связь: {email}",
        settings.EMAIL_HOST_USER,
        [settings.RECIPIENTS_EMAIL],
        fail_silently=False,
    )
    return letter
