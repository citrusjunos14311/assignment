from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import ContactForm
from django.contrib import messages
from django.core.mail import EmailMessage
from django.views.generic import FormView
from django.urls import reverse_lazy

import random

class IndexView(TemplateView):
    template_name='assignment_index.html'

class SecretView(TemplateView):
    template_name='assignment_secret.html'
    def post(self, request, *args, **kwargs):
        if request.POST:
            num = random.randint(1,3)
            if num == 1:
                message1="おまえん家、おっばけや～しき～"
                message2="カンター"
            if num == 2:
                message1="(´･ω･`)"
                message2="　"
            if num == 3:
                message1="残念"
                message2="なにもないぞ"
        context = {
                'message1':message1,
                'message2':message2,
            }
        return render(request, SecretView.template_name, context)

class ContactView(FormView):
    template_name="contact.html"
    form_class=ContactForm
    success_url=reverse_lazy('assignmentapp:contact')
    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        title = form.cleaned_data['title']
        message = form.cleaned_data['message']
        subject = 'お問い合わせ: {}'.format(title)
        message = \
            '送信者名:{0}\nメールアドレス: {1}\n タイトル:{2}\n メッセージ:\{3}' \
            .format(name, email, title, message)
        from_email = 'personalcomputer.citrusjunos@gmail.com'
        to_list = ['personalcomputer.citrusjunos@gmail.com']
        message = EmailMessage(subject=subject,body=message,from_email=from_email,to=to_list,)
        message.send()
        messages.success(self.request, 'お問い合わせは正常に送信されました。')
        return super().form_valid(form)
