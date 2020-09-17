from user.models import User
from user.utils import generate_random_password

from django.http import HttpResponse
# from django.shortcuts import render

from faker import Faker


# Create your views here.

def generate_password(request):
    lenght = int(request.GET.get('len'))
    result = generate_random_password(lenght)
    return HttpResponse(str(result))


def users(request):
    results = ''
    users = User.objects.all()
    for user in users:
        results += f'ID: {user.id}, Email: {user.email}'
    return HttpResponse(results)


def create_user(request):
    fake = Faker()
    user = User.objects.create(
        email=fake.email(),
        first_name=fake.first_name(),
        last_name=fake.last_name(),
    )
    return HttpResponse(f'ID: {user.id} , Email: {user.email}')
