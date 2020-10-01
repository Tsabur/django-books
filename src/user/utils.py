import datetime
import random
import string
from time import sleep
from user.models import Logger

import pytz


def generate_random_password(password_len=10) -> str:
    chars = string.digits + string.ascii_letters + string.punctuation

    result = ""
    for _ in range(password_len):
        result += random.choice(chars)
    return result


def smth_slow(wait=10):
    sleep(wait)


def delete_log():
    date = datetime.datetime.now(pytz.timezone('UTC')) - datetime.timedelta(days=7)
    Logger.objects.filter(created=date).delete()
