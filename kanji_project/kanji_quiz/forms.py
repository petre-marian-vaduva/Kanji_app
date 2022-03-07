from kanji_quiz.models import Kanji, Portuguese
from django import forms
from django.forms import ModelForm

class KanjiForm(forms.ModelForm):
    class Meta:
        model = Kanji
        fields = [
            'character', 'level', 'is_number', 'is_radical'
        ]
        labels = {
            'character': 'Enter a kanji',
            'is_number': 'Is it a number ?',
            'is_radical': 'Is it a radical ?'
        }

        widgets = {
            'character': forms.TextInput(attrs={'placeholder': '漢字'}),
            'example': forms.TextInput(attrs={'placeholder': '漢字'}),
            'is_number': forms.CheckboxInput()

        }

class PortugueseForm(forms.ModelForm):
    class Meta:
        model = Portuguese
        fields = [
            'meaning', 'example'
        ]
        widgets = {
            'example': forms.TextInput(),
        }