from wsgiref.util import request_uri
from django.shortcuts import render
from django.http import HttpResponse
from .models import Kanji, Portuguese
# Create your views here.


def index(request):
    all_kanji = Kanji.objects.all()
    return render(request, 'kanji_quiz/index.html', {
        'all_kanji': all_kanji
    })

def level1(request, slug):
    kanji_level = Kanji.objects.get(pk=slug)
    return render(request, 'kanji_quiz/level1.html')