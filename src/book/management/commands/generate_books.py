from faker import Faker
import random

from book.models import Book
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError


class Command(BaseCommand):

    def handle(self, *args, **options):
        fake = Faker()
        for _ in range(10_000):
            try:
                name = fake.name()
                Book.objects.create(
                    author=fake.name(),
                    title=fake.word(),
                    )
            except IntegrityError:
                print(name)
        print(Book.objects.count())