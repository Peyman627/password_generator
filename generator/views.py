import random

from django.shortcuts import render


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    characters = list('abcdefghijklmnopqrstuvwxys')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    length = int(request.GET.get('length', 12))
    password = ''

    for _ in range(length):
        password += random.choice(characters)

    context = {'password': password}
    return render(request, 'generator/password.html', context)


def about(request):
    return render(request, 'generator/about.html')