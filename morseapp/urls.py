from django.urls import path
from . import views
#from .views import nippo
app_name='morseapp'

urlpatterns=[
    path('',views.IndexView.as_view(),name='index'),
    path('japanese_language_change_morse/',views.JLMorseView.as_view(),name="japanese_language_change_morse"),
    path('morse_change_japanese_language/',views.MorseJLView.as_view(),name="morse_change_japanese_language"),
    path('alphabet_change_morse/',views.AlphabetMorseView.as_view(),name="alphabet_change_morse"),
    path('morse_change_alphabet/',views.MorseAlphabetView.as_view(),name="morse_change_alphabet"),
    path('contact/',views.ContactView.as_view(),name="contact"),
    path('japanese_language/',views.JLView.as_view(),name="japanese_language"),
    path('alphabet/',views.AlphabetView.as_view(),name="alphabet"),
]