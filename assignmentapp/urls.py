from django.urls import path
from . import views
app_name='assignmentapp'

urlpatterns=[
    path('',views.IndexView.as_view(),name='index'),
    path('contact/',views.ContactView.as_view(),name="contact"),
    path('secret/',views.SecretView.as_view(),name='secret'),
]
