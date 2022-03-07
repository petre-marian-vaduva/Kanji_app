from wsgiref.util import request_uri
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from .models import Kanji, Portuguese
from kanji_quiz.forms import KanjiForm, PortugueseForm
from django.urls import reverse
# Create your views here.


def index(request):
    all_kanji = Kanji.objects.all()
    kanji_form = KanjiForm()
    portuguese_form = PortugueseForm()

    if request.method == 'POST':
        kanji_form = KanjiForm(request.POST)
        portuguese_form = PortugueseForm(request.POST)
        if kanji_form.is_valid() and portuguese_form.is_valid():
            kanji_form.save()
            portuguese_form.instance.character = kanji_form.save()
            portuguese_form.save()
            return HttpResponseRedirect('/')

    return render(request, 'kanji_quiz/index.html', {
        'all_kanji': all_kanji,
        'kanji_form': kanji_form,
        'portuguese_form': portuguese_form
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


def update(request, slug):
    all_kanji = Kanji.objects.all()
    row_kanji = Kanji.objects.get(pk=slug)
    form_kanji = KanjiForm(instance=row_kanji)
    row_portuguese = Portuguese.objects.get(character_id=slug)
    form_portuguese = PortugueseForm(instance=row_portuguese)

    if request.method == 'POST':
        form_kanji = KanjiForm(request.POST, instance=row_kanji)
        form_portuguese = PortugueseForm(request.POST, instance=row_portuguese)
        if form_kanji.is_valid():
            form_kanji.save()
            form_portuguese.save()
            return HttpResponseRedirect('/')
    return render(request, 'kanji_quiz/update.html', {
        'form_kanji': form_kanji,
        'form_portuguese': form_portuguese,
        'all_kanji': all_kanji
    })

