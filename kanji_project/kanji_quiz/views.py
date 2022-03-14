from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from .models import Kanji
from kanji_quiz.forms import KanjiForm
from django.urls import reverse
# Create your views here.


def index(request):
    all_kanji = Kanji.objects.all()
    form = KanjiForm()

    if request.method == 'POST':
        form = KanjiForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    return render(request, 'kanji_quiz/index.html', {
        'all_kanji': all_kanji,
        'form': form,
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
    else:
        return render(request, 'kanji_quiz/index.html')

    

def kanji_detail(request, slug):
    kanji = Kanji.objects.get(pk=slug)
    return render(request, 'kanji_quiz/kanji_detail.html', {
        'kanji': kanji
    })


def update(request, slug):
    all_kanji = Kanji.objects.all()
    row_kanji = Kanji.objects.get(pk=slug)
    form = KanjiForm(instance=row_kanji)

    if request.method == 'POST':
        form = KanjiForm(request.POST, instance=row_kanji)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'kanji_quiz/update.html', {
        'form': form,
        'all_kanji': all_kanji
    })

def delete(request, slug):
    kanji = Kanji.objects.get(pk=slug)
    kanji_row = Kanji.objects.get(pk=slug)

    if request.method == 'POST':
        kanji_row.delete()
        return HttpResponseRedirect('/')

    return render(request, 'kanji_quiz/delete.html', {
        'kanji_row': kanji_row, 
        'kanji': kanji
    })

def search(request):
    return render(request, 'kanji_quiz/search.html')