import random
from user.models import User

from django.core.management.base import BaseCommand
# from django.db.utils import IntegrityError

from faker import Faker


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        fake = Faker()
        for poll_id in options['poll_ids']:
            for _ in range(poll_id):
                User.objects.create(
                    email=fake.email(),
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    age=random.randint(1, 100),

                )


'''
    def handle(self, *args, **options):
        fake = Faker()
        for _ in range(10):
            try:
                email = fake.email()
                User.objects.create(
                    email=email,
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    age=random.randint(1, 100),
                    )
            except IntegrityError:
                pass
'''
