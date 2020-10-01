from user.utils import delete_log, smth_slow

from celery import shared_task

from django.core.mail import send_mail


@shared_task
def smth_slow_async(wait=10):
    # print('1'*100)
    smth_slow(wait)


@shared_task
def send_mail_async(subject, text):
    send_mail(
        subject,
        text,
        'testtsabur@gmail.com',
        ['dmytro.kaminskyi92@gmail.com'],
        fail_silently=False,
    )


@shared_task
def delete_log_async():
    delete_log()
