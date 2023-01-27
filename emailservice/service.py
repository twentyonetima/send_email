from django.core.mail import send_mail


def send(user_email):
    send_mail(
        "Send mail",
        "Spam message",
        'your@gmail.com',
        [user_email],
        fail_silently=False,
    )
