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
    if slug == '1': 
        return render(request, 'kanji_quiz/1.html', {
            'all_kanji': all_kanji
        })
    elif slug == '2': 
        return render(request, 'kanji_quiz/2.html', {
            'all_kanji': all_kanji
        })
    elif slug == '3': 
        return render(request, 'kanji_quiz/3.html', {
            'all_kanji': all_kanji
        })
    elif slug == '4': 
        return render(request, 'kanji_quiz/4.html', {
            'all_kanji': all_kanji
        })
    elif slug == '5': 
        return render(request, 'kanji_quiz/5.html', {
            'all_kanji': all_kanji
        })
    elif slug == 'numbers':
        return render(request, 'kanji_quiz/numbers.html', {
            'all_kanji': all_kanji
        })

def kanji_detail(request, slug):
    kanji = Kanji.objects.get(pk=slug)
    kanji_meaning = kanji.portuguese_set.all()
    return render(request, 'kanji_quiz/kanji_detail.html', {
        'kanji': kanji,
        'kanji_meaning': kanji_meaning
    })

