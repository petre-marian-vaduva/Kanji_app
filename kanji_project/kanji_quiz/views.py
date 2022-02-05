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

def level(request, slug):
    all_kanji = Kanji.objects.all()
    if slug == 'level1': 
        return render(request, 'kanji_quiz/level1.html', {
            'all_kanji': all_kanji
        })
    elif slug == 'level2': 
        return render(request, 'kanji_quiz/level2.html', {
            'all_kanji': all_kanji
        })
    elif slug == 'level3': 
        return render(request, 'kanji_quiz/level3.html', {
            'all_kanji': all_kanji
        })
    elif slug == 'level4': 
        return render(request, 'kanji_quiz/level4.html', {
            'all_kanji': all_kanji
        })
    elif slug == 'level5': 
        return render(request, 'kanji_quiz/level5.html', {
            'all_kanji': all_kanji
        })

def kanji_detail(request, slug):
    kanji = Kanji.objects.get(pk=slug)
    kanji_meaning = kanji.portuguese_set.all()
    return render(request, 'kanji_quiz/kanji_detail.html')
