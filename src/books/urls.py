"""books URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from user import views as uv

from book import views as bv

from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', uv.index),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('generate-password/', uv.generate_password),
    path('users-list/', uv.users, name='users-name'),
    path('create-user/', uv.create_user, name='users-create'),
    path('update-user/<int:pk>/', uv.update_user, name='users-update'),
    # path('/asd/',TemplateView.as_view(template_name='index_book.html'), name='index-book'),
    path('books/create/', bv.books_create, name='books-create'),
    path('books/update/<int:pk>/', bv.update_book, name='books-update'),
    path('books/delete/<int:pk>/', bv.delete_book, name='books-delete'),
    path('books/list/', bv.book_list, name='books-name'),

]

from django.conf import settings
from django.urls import include, path

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
