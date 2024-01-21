from django.forms import ModelForm
from .models import Quiz

class QuizForm(ModelForm):
    class Meta:
        model=Quiz
        fields=['category','quiz','answer']

