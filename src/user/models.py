from django.db import models

# Create your models here.


class User(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    age = models.PositiveSmallIntegerField(default=0)
    phone = models.CharField(max_length=30, default='None')

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name},  Phone: {self.phone}'

    def save(self, *args, **kwargs):
        # self.email = self.email.lower()
        # self.first_name = self.first_name.title()
        # self.last_name = self.last_name.title()
        super().save(*args, **kwargs)


class Logger(models.Model):
    method = models.CharField(max_length=256)
    path = models.CharField(max_length=256)
    response_time = models.CharField(max_length=256)
    created = models.CharField(max_length=256)
