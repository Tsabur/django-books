from django.db import models

# Create your models here.


class Book(models.Model):
    author = models.CharField(max_length=128)
    title = models.CharField(max_length=128)

    def info(self):
        return f'{self.author}, Title: {self.title}'
