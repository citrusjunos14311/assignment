from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse_lazy
from .form import ContactForm

from django.contrib import messages
from django.core.mail import EmailMessage

from django.views.generic.base import TemplateView

import random

class IndexView(TemplateView):
    template_name="morse_index.html"
    def post(self, request, *args, **kwargs):
        if request.POST:
            message=""
            url=""
            go=""
            img=""
            num = random.randint(1,12)
            #switchが欲しい
            if num == 1:
                message="何で押したん？"
            if num == 2:
                message="押したくなるよね"
            if num == 3:
                message="何回も押すなよ"
            if num == 4:
                n = random.randint(1,3)
                go='押してみな飛ぶぞ{}'.format(n)
                if n==1:
                    url='https://www.yahoo.co.jp/'
                if n==2:
                    url='https://www.amazon.co.jp/'
                if n==3:
                    url='https://www.youtube.com/'
            if num == 5:
                img="../static/images/book_fukayomi.png"
            if num == 6:
                message="しかし何も起こらなかった"
            context = {
                'coment': message,
                'website': url,
                "go": go,
                'img':img,
            }
        return render(request, IndexView.template_name, context)

"""class TestView(TemplateView):
    template_name="test.html"
    message=""
    def post(self, request, *args, **kwargs):
        messagepost=JLMorseView.message
        if request.POST:
            messagepost = request.POST["name1"]
            messageget=messagepost
            context = {
            'messagepost': messagepost,
            'messageget': messageget,
        }
        return render(request, TestView.template_name, context)"""

class JLMorseView(TemplateView):
    template_name="japanese_language_change_morse.html"
    message=""
 
    def post(self, request, *args, **kwargs):
        messagepost=JLMorseView.message
        if request.POST:
            messagepost = request.POST["name1"]
            
            messageget=messagepost
            name=list(messageget)
            x=len(name)
            n=0
            i=0
            moji=['あ','い','う','え','お',
                  'か','き','く','け','こ',
                  'さ','し','す','せ','そ',
                  'た','ち','つ','て','と',
                  'な','に','ぬ','ね','の',
                  'は','ひ','ふ','へ','ほ',
                  'ま','み','む','め','も',
                  'や','ゆ','よ',
                  'ら','り','る','れ','ろ',
                  'わ','を','ん',
                  'が','ぎ','ぐ','げ','ご',
                  'ざ','じ','ず','ぜ','ぞ',
                  'だ','ぢ','づ','で','ど',
                  'ば','び','ぶ','べ','ぼ',
                  'ぱ','ぴ','ぷ','ぺ','ぽ',
                  '、','。','ー',]
            morse = ['ーー・ーー', '・ー', '・・ー', 'ー・ーーー', '・ー・・・',#あ行
                     '・ー・・', 'ー・ー・・', '・・・ー', 'ー・ーー', 'ーーーー',#か行
                     'ー・ー・ー', 'ーー・ー・', 'ーーー・ー', '・ーーー・', 'ーーー・',#さ行
                     'ー・', '・・ー・', '・ーー・', '・ー・ーー', '・・ー・・',#た行
                     '・ー・', 'ー・ー・', '・・・・', 'ーー・ー', '・・ーー',#な行
                     'ー・・・', 'ーー・・ー', 'ーー・・', '・', 'ー・・',#は行
                     'ー・・ー', '・・ー・ー', 'ー', 'ー・・・ー', 'ー・・ー・',#ま行
                     '・ーー', 'ー・・ーー', 'ーー',#や行
                     '・・・', 'ーー・', 'ー・ーー・', 'ーーー', '・ー・ー',#ら行
                     'ー・ー', '・ーーー', '・ー・ー・',#わ行
                     '・ー・・,・・', 'ー・ー・・,・・', '・・・ー,・・', 'ー・ーー,・・', 'ーーーー,・・',#が行
                     'ー・ー・ー,・・', 'ーー・ー・,・・', 'ーーー・ー,・・', '・ーーー・,・・', 'ーーー・,・・',#ざ行
                     'ー・,・・', '・・ー・,・・', '・ーー・,・・', '・ー・ーー,・・', '・・ー・・,・・',#だ行
                     'ー・・・,・・', 'ーー・・ー,・・', 'ーー・・,・・', '・,・・', 'ー・・,・・',#ば行
                     'ー・・・,・・ーー・', 'ーー・・ー,・・ーー・', 'ーー・・,・・ーー・,・・ーー・', '・,・・ーー・', 'ー・・,・・ーー・',#ぱ行
                     '・ー・ー・ー', '', '・ーー・ー',]
            r=[]
            for i in range(x):#while i<=x:
                for n in range(72):#while n <= 60:
                    if(name[i]==moji[n]):
                        r.append(morse[n])
                        r.append(',')
                    n+=1
                i=i+1
            l=''.join(r)
            messageget=l
        context = {
            'messagepost': messagepost,
            'messageget': messageget,
        }
        return render(request, JLMorseView.template_name, context)

class MorseJLView(TemplateView):
    template_name="morse_change_japanese_language.html"
    message=""
 
    def post(self, request, *args, **kwargs):
        messagepost=MorseJLView.message
        if request.POST:
            messagepost = request.POST["name1"]
            messageget=messagepost
            morse = ['ーー・ーー', '・ー', '・・ー', 'ー・ーーー', '・ー・・・',#あ行
                     '・ー・・', 'ー・ー・・', '・・・ー', 'ー・ーー', 'ーーーー',#か行
                     'ー・ー・ー', 'ーー・ー・', 'ーーー・ー', '・ーーー・', 'ーーー・',#さ行
                     'ー・', '・・ー・', '・ーー・', '・ー・ーー', '・・ー・・',#た行
                     '・ー・', 'ー・ー・', '・・・・', 'ーー・ー', '・・ーー',#な行
                     'ー・・・', 'ーー・・ー', 'ーー・・', '・', 'ー・・',#は行
                     'ー・・ー', '・・ー・ー', 'ー', 'ー・・・ー', 'ー・・ー・',#ま行
                     '・ーー', 'ー・・ーー', 'ーー',#や行
                     '・・・', 'ーー・', 'ー・ーー・', 'ーーー', '・ー・ー',#ら行
                     'ー・ー', '・ーーー', '・ー・ー・',#わ行
                     '・ー・・,・・', 'ー・ー・・,・・', '・・・ー,・・', 'ー・ーー,・・', 'ーーーー,・・',#が行
                     'ー・ー・ー,・・', 'ーー・ー・,・・', 'ーーー・ー,・・', '・ーーー・,・・', 'ーーー・,・・',#ざ行
                     'ー・,・・', '・・ー・,・・', '・ーー・,・・', '・ー・ーー,・・', '・・ー・・,・・',#だ行
                     'ー・・・,・・', 'ーー・・ー,・・', 'ーー・・,・・', '・,・・', 'ー・・,・・',#ば行
                     'ー・・・,・・ーー・', 'ーー・・ー,・・ーー・', 'ーー・・,・・ーー・,・・ーー・', '・,・・ーー・', 'ー・・,・・ーー・',#ぱ行
                     '・ー・ー・ー', '', '・ーー・ー',]
            moji=['あ','い','う','え','お',
                  'か','き','く','け','こ',
                  'さ','し','す','せ','そ',
                  'た','ち','つ','て','と',
                  'な','に','ぬ','ね','の',
                  'は','ひ','ふ','へ','ほ',
                  'ま','み','む','め','も',
                  'や','ゆ','よ',
                  'ら','り','る','れ','ろ',
                  'わ','を','ん',
                  'が','ぎ','ぐ','げ','ご',
                  'ざ','じ','ず','ぜ','ぞ',
                  'だ','ぢ','づ','で','ど',
                  'ば','び','ぶ','べ','ぼ',
                  'ぱ','ぴ','ぷ','ぺ','ぽ',
                  '、','。','ー',]
            
            name=list(messageget)
            name.append(',')
            x=len(name)
            ja=[]
            n=0
            d=0
            for p in range(x):
                if name[p]==',':
                    d=d+1
            for f in range(d):
                r=[]
                while name[n]!=',':
                    r.append(name[n])
                    n=n+1
                r=''.join(r)
                if name[n] ==',':
                    n=n+1
                for i in range(72):
                    if r==morse[i]:
                        ja.append(moji[i])

            l=''.join(ja)
            messageget=l
        context = {
            'messagepost': messagepost,
            'messageget': messageget,
        }
        return render(request, MorseJLView.template_name, context)

class AlphabetMorseView(TemplateView):
    template_name="alphabet_change_morse.html"
    message=""
 
    def post(self, request, *args, **kwargs):
        messagepost=AlphabetMorseView.message
        if request.POST:
            messagepost = request.POST["name1"]
            
            messageget=messagepost
            morse=['・ー','ー・・・','ー・ー・','ー・・','・',#ABCDE
                   '・・ー・','ーー・','・・・・','・・','・ーーー',#FGHIJ
                   'ー・－','・ー・・','ーー','ー・','ーーー',#KLMNO
                   '・ーー・','ーー・ー','・ー・','・・・','ー',#PQRST
                   '・・ー','・・・ー','・ーー','ー・・ー','ー・ーー',#UVWXY
                   'ーー・・',]#Z
            moji=['a','b','c','d','e',
                  'f','j','h','i','j',
                  'k','l','m','n','o',
                  'p','q','r','s','t',
                  'u','v','w','x','y',
                  'z',]
            MOJI=['A','B','C','D','E',
                  'F','G','H','I','J',
                  'K','L','M','N','O',
                  'P','Q','R','S','T',
                  'U','V','W','X','Y',
                  'Z',]
            name=messageget
            name=list(name)
            x=len(name)
            n=0
            i=0
            r=[]
            for i in range(x):
                for n in range(26):
                    if(name[i]==moji[n] or name[i]==MOJI[n]):
                        r.append(morse[n])
                        r.append(',')
                    n+=1
                i=i+1
            l=''.join(r)
            messageget=l
        context = {
            'messagepost': messagepost,
            'messageget': messageget,
        }
        return render(request, AlphabetMorseView.template_name, context)

class MorseAlphabetView(TemplateView):
    template_name="morse_change_alphabet.html"
    message=""
 
    def post(self, request, *args, **kwargs):
        messagepost=MorseAlphabetView.message
        if request.POST:
            messagepost = request.POST["name1"]
            
            messageget=messagepost
            morse=['・ー','ー・・・','ー・ー・','ー・・','・',#ABCDE
                   '・・ー・','ーー・','・・・・','・・','・ーーー',#FGHIJ
                   'ー・－','・ー・・','ーー','ー・','ーーー',#KLMNO
                   '・ーー・','ーー・ー','・ー・','・・・','ー',#PQRST
                   '・・ー','・・・ー','・ーー','ー・・ー','ー・ーー',#UVWXY
                   'ーー・・',]#Z
            moji=['a','b','c','d','e',
                  'f','j','h','i','j',
                  'k','l','m','n','o',
                  'p','q','r','s','t',
                  'u','v','w','x','y',
                  'z',]
            """MOJI=['A','B','C','D','E',
                  'F','G','H','I','J',
                  'K','L','M','N','O',
                  'P','Q','R','S','T',
                  'U','V','W','X','Y',
                  'Z',]"""
            
            name=list(messageget)
            name.append(',')
            x=len(name)
            en=[]
            n=0
            d=0
            for p in range(x):
                if name[p]==',':
                    d=d+1
            for f in range(d):
                r=[]
                while name[n]!=',':
                    r.append(name[n])
                    n=n+1
                r=''.join(r)
                if name[n] ==',':
                    n=n+1
                for i in range(26):
                    if r==morse[i]:
                        en.append(moji[i])

            l=''.join(en)
            messageget=l
        context = {
            'messagepost': messagepost,
            'messageget': messageget,
        }
        return render(request, MorseAlphabetView.template_name, context)
    
class ContactView(FormView):
    template_name="contact.html"
    form_class=ContactForm
    success_url=reverse_lazy('morseapp:contact')
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

class JLView(TemplateView):
    template_name="japanese_language.html"
    text=""
    morse = ['ーー・ーー', '・ー', '・・ー', 'ー・ーーー', '・ー・・・',#あ行
             '・ー・・', 'ー・ー・・', '・・・ー', 'ー・ーー', 'ーーーー',#か行
             'ー・ー・ー', 'ーー・ー・', 'ーーー・ー', '・ーーー・', 'ーーー・',#さ行
             'ー・', '・・ー・', '・ーー・', '・ー・ーー', '・・ー・・',#た行
             '・ー・', 'ー・ー・', '・・・・', 'ーー・ー', '・・ーー',#な行
             'ー・・・', 'ーー・・ー', 'ーー・・', '・', 'ー・・',#は行
             'ー・・ー', '・・ー・ー', 'ー', 'ー・・・ー', 'ー・・ー・',#ま行
             '・ーー', 'ー・・ーー', 'ーー',#や行
             '・・・', 'ーー・', 'ー・ーー・', 'ーーー', '・ー・ー',#ら行
             'ー・ー', '・ーーー', '・ー・ー・',#わ行
             '・ー・・,・・', 'ー・ー・・,・・', '・・・ー,・・', 'ー・ーー,・・', 'ーーーー,・・',#が行
             'ー・ー・ー,・・', 'ーー・ー・,・・', 'ーーー・ー,・・', '・ーーー・,・・', 'ーーー・,・・',#ざ行
             'ー・,・・', '・・ー・,・・', '・ーー・,・・', '・ー・ーー,・・', '・・ー・・,・・',#だ行
             'ー・・・,・・', 'ーー・・ー,・・', 'ーー・・,・・', '・,・・', 'ー・・,・・',#ば行
             'ー・・・,・・ーー・', 'ーー・・ー,・・ーー・', 'ーー・・,・・ーー・,・・ーー・', '・,・・ーー・', 'ー・・,・・ーー・',#ぱ行
             '・ー・ー・ー', '', '・ーー・ー',]
    moji=['あ','い','う','え','お',
          'か','き','く','け','こ',
          'さ','し','す','せ','そ',
          'た','ち','つ','て','と',
          'な','に','ぬ','ね','の',
          'は','ひ','ふ','へ','ほ',
          'ま','み','む','め','も',
          'や','ゆ','よ',
          'ら','り','る','れ','ろ',
          'わ','を','ん',
          'が','ぎ','ぐ','げ','ご',
          'ざ','じ','ず','ぜ','ぞ',
          'だ','ぢ','づ','で','ど',
          'ば','び','ぶ','べ','ぼ',
          'ぱ','ぴ','ぷ','ぺ','ぽ',
          '、','。','ー',]
    def post(self, request, *args, **kwargs):
        Original_text=JLView.text
        if request.POST:
            Original_text = request.POST["name1"]
            Translation=Original_text
            m=list(Original_text)
            g=0
            u=0
            t=0
            while(72>=t):
                if m[0]==JLView.moji[t]:
                    g+=1
                t=t+1
            if g==1:
                name=list(Translation)
                x=len(name)
                n=0
                i=0
                #mojimorse
                r=[]
                for i in range(x):
                    for n in range(72):
                        if(name[i]==JLView.moji[n]):
                            r.append(JLView.morse[n])
                            r.append(',')
                        n+=1
                    i=i+1
                l=''.join(r)
                Translation=l
            t=0
            while(72>=t):
                if m[0]==JLView.morse[t]:
                    u+=1
                t=t+1
            if u==1:
               #morsemoji
                name=list(Translation)
                name.append(',')
                x=len(name)
                ja=[]
                n=0
                d=0
                for p in range(x):
                    if name[p]==',':
                        d=d+1
                for f in range(d):
                    r=[]
                    while name[n]!=',':
                        r.append(name[n])
                        n=n+1
                    r=''.join(r)
                    if name[n] ==',':
                        n=n+1
                    for i in range(72):
                        if r==JLView.morse[i]:
                            ja.append(JLView.moji[i])
                l=''.join(ja)
                Translation=l
            context = {
            'messagepost': Original_text,
            'messageget': Translation,
        }
        return render(request, JLView.template_name, context)

class AlphabetView(TemplateView):
    template_name="alphabet.html"
    text=""
    morse=['・ー','ー・・・','ー・ー・','ー・・','・',#ABCDE
           '・・ー・','ーー・','・・・・','・・','・ーーー',#FGHIJ
           'ー・－','・ー・・','ーー','ー・','ーーー',#KLMNO
           '・ーー・','ーー・ー','・ー・','・・・','ー',#PQRST
           '・・ー','・・・ー','・ーー','ー・・ー','ー・ーー',#UVWXY
           'ーー・・',]#Z
    moji=['a','b','c','d','e',
          'f','j','h','i','j',
          'k','l','m','n','o',
          'p','q','r','s','t',
          'u','v','w','x','y',
          'z',]
    MOJI=['A','B','C','D','E',
          'F','G','H','I','J',
          'K','L','M','N','O',
          'P','Q','R','S','T',
          'U','V','W','X','Y',
          'Z',]
    def post(self, request, *args, **kwargs):
        Original_text=AlphabetView.text
        if request.POST:
            Original_text = request.POST["name1"]
            Translation=Original_text
            m=list(Original_text)
            g=0
            u=0
            t=0
            while(t<=25):
                if m[0]==AlphabetView.moji[t] or m[0]==AlphabetView.MOJI[t]:
                    g+=1
                t+=1
            if g==1:
                name=Translation
                name=list(name)
                x=len(name)
                n=0
                i=0
                r=[]
                for i in range(x):
                    for n in range(26):
                        if(name[i]==AlphabetView.moji[n] or name[i]==AlphabetView.MOJI[n]):
                            r.append(AlphabetView.morse[n])
                            r.append(',')
                        n+=1
                    i=i+1
                l=''.join(r)
                Translation=l
            t=0
            while(t<=25):
                if m[0]==AlphabetView.morse[t]:
                    u+=1
                t+=1
            if u==1:
                name=list(Translation)
                name.append(',')
                x=len(name)
                en=[]
                n=0
                d=0
                for p in range(x):
                    if name[p]==',':
                        d=d+1
                for f in range(d):
                    r=[]
                    while name[n]!=',':
                        r.append(name[n])
                        n=n+1
                    r=''.join(r)
                    if name[n] ==',':
                        n=n+1
                    for i in range(26):
                        if r==AlphabetView.morse[i]:
                            en.append(AlphabetView.moji[i])
                l=''.join(en)
                Translation=l
        context = {
            'messagepost': Original_text,
            'messageget': Translation,
        }
        return render(request, AlphabetView.template_name, context)
