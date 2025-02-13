from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def send_email(request):
    if request.method == 'POST':
        recipient = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        
        send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient])
        
        return render(request, 'emails/success.html', {'email': recipient})
    
    return render(request, 'emails/send_email.html')
