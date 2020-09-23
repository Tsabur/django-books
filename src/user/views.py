from user.forms import UserForm
from user.models import User
from user.utils import generate_random_password

from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect

# from faker import Faker
# from django.http import Http404

# Create your views here.


def generate_password(request):
    lenght = int(request.GET.get('len'))
    result = generate_random_password(lenght)
    return HttpResponse(str(result))


def users(request):
    context ={
        'user_list': User.objects.all(),
    }
    return render(request, 'list_users.html', context=context)


def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponseRedirect(reverse('users-name'))
            return redirect('users-name')
    elif request.method == 'GET':
        form = UserForm()
    context = {'user_form': form}
    return render(request, 'create_user.html', context=context)


def update_user(request, pk):

    # try:
    #     user = User.odjects.get(pk=pk)
    # except User.DoesNotExist:
    #     raise Http404

    user = get_object_or_404(User, pk=pk)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            # return HttpResponseRedirect(reverse('users-name'))
            return redirect('users-name')
    elif request.method == 'GET':
        form = UserForm(instance=user)

    context = {
        'user_form': form,
        'user_instance': user,
    }
    return render(request, 'create_user.html', context=context)


def index(request):
    return render(request, 'index.html')


'''
def create_user(request):
    fake = Faker()
    user = User.objects.create(
        email=fake.email(),
        first_name=fake.first_name(),
        last_name=fake.last_name(),
    )
    return HttpResponse(f'ID: {user.id} , Email: {user.email}')
'''
