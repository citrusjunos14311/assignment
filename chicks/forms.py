from django.forms import ModelForm
from .models import ChickPost,Comment,Category
from django import forms

class ChickPostForm(ModelForm):
    class Meta:
        model=ChickPost
        fields=['category','title','comment','image']

class ChickCommentForm(ModelForm):
    class Meta:
        model=Comment
        fields=['post','thoughts_on_comment','comment_image']

class ChickCategoryForm(ModelForm):
    class Meta:
        model=Category
        fields=['title']

class ContactForm(forms.Form):
    name = forms.CharField(label='お名前')
    email = forms.EmailField(label='メールアドレス')
    title = forms.CharField(label='件名')
    message = forms.CharField(label='メッセージ', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = \
        'お名前を入力してください'
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = \
        'メールアドレスを入力してください'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['placeholder'] = \
        'タイトルを入力してください'
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['placeholder'] = \
        'メッセージを入力してください'
        self.fields['message'].widget.attrs['class'] = 'form-control'