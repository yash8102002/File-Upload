import os
from django.conf import settings
from django.shortcuts import render
from .tasks import send_email_with_attachment  # Import your celery task

def upload_file(request):
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']

        # Ensure media directory exists
        os.makedirs(settings.MEDIA_ROOT, exist_ok=True)

        save_path = os.path.join(settings.MEDIA_ROOT, uploaded_file.name)

        with open(save_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        # Call celery task to send email asynchronously
        send_email_with_attachment.delay(save_path, uploaded_file.name, 'yp650213@gmail.com')

        return render(request, 'upload_success.html')

    return render(request, 'upload_form.html')
