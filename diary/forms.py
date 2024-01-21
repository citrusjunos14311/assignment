from django.forms import ModelForm
from .models import Diary,DiaryGood
from django import forms

class DiaryForm(ModelForm):
    class Meta:
        model=Diary
        fields=['title','sentence']

class DiaryGoodForm(ModelForm):
    class Meta:
        model=DiaryGood
        fields=['post']
