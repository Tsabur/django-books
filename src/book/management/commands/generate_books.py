from book.models import Book

from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

from faker import Faker


class Command(BaseCommand):

    def handle(self, *args, **options):
        fake = Faker()
        for _ in range(10_000):
            try:
                name = fake.name()
                Book.objects.create(
                    author=name,
                    title=fake.word(),
                    )
            except IntegrityError:
                pass
#               print(name)
