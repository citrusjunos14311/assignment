from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .models import Quiz

from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import QuizForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.views.generic import DetailView
from django.views.generic import DeleteView

class QuizIndexView(ListView):
    template_name="quiz.html"
    queryset=Quiz.objects.order_by('-posted_at')
    paginate_by=30

class QuizPostSuccessView(TemplateView):
    template_name='quiz_post_success.html'

class QuizUserView(ListView):
    template_name='quiz.html'
    paginate_by=30
    def get_queryset(self):
        user_id=self.kwargs['user']
        user_list=Quiz.objects.filter(user=user_id).order_by('-posted_at')
        return user_list

class QuizMypageView(ListView):
    template_name='quiz_mypage.html'
    paginate_by=30
    def get_queryset(self):
        queryset=Quiz.objects.filter(user=self.request.user).order_by('-posted_at')
        return queryset

@method_decorator(login_required,name='dispatch')
class CreateQuizView(CreateView):
    form_class=QuizForm
    template_name="post_quiz.html"
    success_url=reverse_lazy('quiz:post_quiz_success')
    def form_valid(self,form):
        postdata=form.save(commit=False)
        postdata.user=self.request.user
        postdata.save()
        return super().form_valid(form)
    
class QuizDeleteView(DeleteView):
    model=Quiz
    template_name='quiz_delete.html'
    success_url=reverse_lazy('quiz:quiz_mypage')
    def delete(self,request,*args,**kwargs):
        return super().delete(request,*args,**kwargs)
    
class QuizDetailView(DetailView):
    template_name='quiz_detail.html'
    model=Quiz

class AnswerDetailView(DetailView):
    template_name='answer_detail.html'
    model=Quiz