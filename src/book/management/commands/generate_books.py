from book.models import Book, Category

from django.core.management.base import BaseCommand
# from django.db.utils import IntegrityError

from faker import Faker


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('poll_ids', nargs='?', type=int, default=500)

    def handle(self, *args, **options):
        fake = Faker()
        Book.objects.all().delete()
        # breakpoint()
        count = options['poll_ids']
        for i in range(count):
            Category.objects.create(
                name=fake.word(),
            )

        for _ in range(count):
            name = Category.objects.order_by('?').last()
            Book.objects.create(
                author=fake.name(),
                title=fake.word(),
                category=name,
            )

# class Command(BaseCommand):
#
#     def handle(self, *args, **options):
#         fake = Faker()
#         for _ in range(10_000):
#             try:
#                 name = fake.name()
#                 Book.objects.create(
#                     author=name,
#                     title=fake.word(),
#                     )
#             except IntegrityError:
#                 pass
# #               print(name)
