#from django.test import TestCase

# Create your tests here.
"""
name='あかさたながざ'
name=list(name)
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
morse = ['ーー・－－', '・－', '・・－', 'ー・－－－', '・－・・・',#あ行
         '・－・・', 'ー・－・・', '・・・－', 'ー・－－', 'ーーーー',#か行
         'ー・－・－', 'ーー・－・', 'ーーー・－', '・－－－・', 'ーーー・',#さ行
         'ー・', '・・－・', '・－－・', '・－・－－', '・・－・・',#た行
         '・－・', 'ー・－・', '・・・・', 'ーー・－', '・・－－',#な行
         'ー・・・', 'ーー・・－', 'ーー・・', '・', 'ー・・',#は行
         'ー・・－', '・・－・－', 'ー', 'ー・・・－', 'ー・・－・',#ま行
         '・－－', 'ー・・－－', 'ーー',#や行
         '・・・', 'ーー・', 'ー・－－・', 'ーーー', '・－・－',#ら行
         'ー・－', '・－－－', '・－・－・',#わ行
         '・－・・,・・', 'ー・－・・,・・', '・・・－,・・', 'ー・－－,・・', 'ーーーー,・・',#が行
         'ー・－・－,・・', 'ーー・－・,・・', 'ーーー・－,・・', '・－－－・,・・', 'ーーー・,・・',#ざ行
         'ー・,・・', '・・－・,・・', '・－－・,・・', '・－・－－,・・', '・・－・・,・・',#だ行
         'ー・・・,・・', 'ーー・・－,・・', 'ーー・・,・・', '・,・・', 'ー・・,・・',#ば行
         'ー・・・,・・－－・', 'ーー・・－,・・－－・', 'ーー・・,・・－－・,・・－－・', '・,・・－－－・', 'ー・・,・・－－・',#ぱ行
         '・－・－・－', '', '・－－・－',]
r=[]
for i in range(x):#while i<=x:
    for n in range(72):#while n <= 60:
        if(name[i]==moji[n]):
            r.append(morse[n])
            r.append(',')
        n+=1
    i=i+1

l=''.join(r)
print(l)


"""
#--------------------------------------------------------------------------------
"""
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
name='ーー・ーー,・ー,ーー・・'
name=list(name)
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
print(l)
"""
#------------------------------------------------------------------------
"""
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

name='ABCDEFJHIJKLMNOPQRSTUVWXYZ'
name=list(name)
x=len(name)
n=0
i=0
r=[]
for i in range(x):#while i<=x:
    for n in range(26):#while n <= 60:
        if(name[i]==moji[n]):
            r.append(morse[n])
            r.append(',')
        n+=1
    i=i+1

l=''.join(r)
print(l)
"""