from book.models import Book

from django.http import HttpResponse
# from django.shortcuts import render

from faker import Faker


# Create your views here.
def books_create(request):
    fake = Faker()
    book = Book.objects.create(
        author=fake.name(),
        title=fake.word(),
    )
    return HttpResponse(f'Author: {book.author} , Title: {book.title}')


def book_list(request):
    results = ''
    books = Book.objects.all()
    for book in books:
        results += f'ID: {book.id}, Title: {book.title}'
    return HttpResponse(results)
