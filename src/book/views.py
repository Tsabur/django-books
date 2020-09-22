from book.forms import BookForm
from book.models import Book

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

# from django.http import Http404
# from faker import Faker


# Create your views here.

# def books_create(request):
#     fake = Faker()
#     book = Book.objects.create(
#         author=fake.name(),
#         title=fake.word(),
#     )
#     return HttpResponse(f'Author: {book.author} , Title: {book.title}')

def books_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/books/list/')
    elif request.method == 'GET':
        form = BookForm()
    context = {'book_form': form}
    return render(request, 'create_book.html', context=context)


def update_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/books/list/')
    elif request.method == 'GET':
        form = BookForm(instance=book)
    context = {'book_form': form}
    return render(request, 'create_book.html', context=context)


def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            rem = Book.objects.get(pk=pk)
            rem.delete()
            return HttpResponseRedirect('/books/list/')
    else:
        form = BookForm(instance=book)
        context = {'book_form': form}
        return render(request, 'create_book.html', context=context)


def book_list(request):
    results = ''
    books = Book.objects.all()
    for book in books:
        results += f'ID: {book.id}, Title: {book.title}'
    return HttpResponse(results)
