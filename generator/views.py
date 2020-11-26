from django.shortcuts import render


# Create your views here.
def home(request):
    context = {'password': 'hsfsdg243*ds'}
    return render(request, 'generator/home.html', context)
