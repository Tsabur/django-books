from django.db import models

# Create your models here.


class Book(models.Model):
    author = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    category = models.ForeignKey('book.Category',
                                 related_name='books',
                                 on_delete=models.SET_NULL, null=True)

    def info(self):
        return f'{self.author}, Title: {self.title}'


class Category(models.Model):
    name = models.CharField(max_length=128)
