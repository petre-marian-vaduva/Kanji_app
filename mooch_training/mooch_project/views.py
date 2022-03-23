from django import shortcuts
from django.shortcuts import render


def home(request):
    return render(request,'mooch/default_webpage.html')



