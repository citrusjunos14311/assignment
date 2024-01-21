from django.urls import path
from . import views
app_name='quiz'

urlpatterns=[
    path('',views.QuizIndexView.as_view(),name="index"),
    path('post_quiz_success/',views.QuizPostSuccessView.as_view(),name="post_quiz_success"),
    path('quiz_mypage/',views.QuizMypageView.as_view(),name="quiz_mypage"),
    path('user_list/<int:user>',views.QuizUserView.as_view(),name='user_list'),
    path('post_quiz/',views.CreateQuizView.as_view(),name="post_quiz"),
    path('quiz/<int:pk>/delete/',views.QuizDeleteView.as_view(),name="quiz_delete"),
    path('quiz_detail/<int:pk>',views.QuizDetailView.as_view(),name='quiz_detail'),
    path('answer_detail/<int:pk>',views.AnswerDetailView.as_view(),name="answer_detail"),
]