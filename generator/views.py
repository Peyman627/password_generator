from django.shortcuts import render


def home(request):
    context = {'password': 'hsfsdg243*ds'}
    return render(request, 'generator/home.html', context)


def password(request):
    return render(request, 'generator/password.html')