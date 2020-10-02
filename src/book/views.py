from book.forms import BookForm
from book.models import Book, Category

from django.shortcuts import get_object_or_404, redirect, render

# from django.urls import reverse
# from faker import Faker
# from django.http import Http404
# from django.http import HttpResponse
# from django.http import HttpResponseRedirect

# Create your views here.

# def books_create(request):
#     fake = Faker()
#     book = Book.objects.create(
#         author=fake.name(),
#         title=fake.word(),
#     )
#     return HttpResponse(f'Author: {book.author} , Title: {book.title}')


def category_list(request):
    categorys_queryset = Category.objects.all().prefetch_related('books')
    context = {
        'category_list': categorys_queryset,
    }
    return render(request, 'list_category.html', context=context)


def book_list(request):
    context = {
        'book_list': Book.objects.all(),
    }
    return render(request, 'list_book.html', context=context)


def book_list_category(request):
    books_queryset = Book.objects.all()\
        .only('id', 'title', 'category__name')\
        .select_related('category')
    context = {
        'book_list': books_queryset,
    }
    return render(request, 'list_book_category.html', context=context)


# .defer('author', вводить поля которые надо исключить) <- используется вместо .only


def books_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponseRedirect('/books/list/')
            return redirect('books-name')
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
            # return HttpResponseRedirect('/books/list/')
            return redirect('books-name')
    elif request.method == 'GET':
        form = BookForm(instance=book)

    context = {
        'book_form': form,
        'book_instance': book,

    }
    return render(request, 'create_book.html', context=context)


def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            rem = Book.objects.get(pk=pk)
            rem.delete()
            # return HttpResponseRedirect('/books/list/')
            return redirect('books-name')
    else:
        form = BookForm(instance=book)
        context = {'book_form': form}
        return render(request, 'create_book.html', context=context)
