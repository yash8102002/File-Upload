from celery import shared_task
from django.core.mail import EmailMessage
from django.conf import settings

@shared_task
def send_email_with_attachment(file_path, filename, recipient_email):
    email = EmailMessage(
        subject=f'Uploaded file: {filename}',
        body=f'The file "{filename}" has been uploaded. See attached.',
        from_email=settings.EMAIL_HOST_USER,
        to=[recipient_email],
    )
    email.attach_file(file_path)
    email.send()
