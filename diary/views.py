from django.views import View
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView

from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import DiaryForm,DiaryGoodForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import Diary,DiaryGood

from django.views.generic import DetailView

from django.views.generic import DeleteView


class DiaryIndexView(ListView):
    template_name="diary.html"
    queryset=Diary.objects.order_by('-posted_at')
    paginate_by=30

@method_decorator(login_required,name='dispatch')
class CreateChickView(CreateView):
    form_class=DiaryForm
    template_name="post_diary.html"
    success_url=reverse_lazy('diary:post_done')
    def form_valid(self,form):
        postdata=form.save(commit=False)
        postdata.user=self.request.user
        postdata.save()
        return super().form_valid(form)

class PostSuccessView(TemplateView):
    template_name='diary_post_success.html'

@method_decorator(login_required,name='dispatch')
class ChickCommentView(CreateView,View):
    form_class=DiaryGoodForm
    template_name='post_diarygood.html'
    success_url=reverse_lazy('diary:post_done')
    def get(self, request, pk, *args, **kwargs):
        context = {}
        context["ChickPost"]  = Diary.objects.filter(id=pk).first()
        context["Comment"]  = DiaryGood.objects.filter(post=pk)
        context["form"]     = DiaryGoodForm
        return render(request,"post_diarygood.html",context)
    def form_valid(self, form):
        postdata=form.save(commit=False)
        postdata.good_user=self.request.user
        postdata.save()
        return super().form_valid(form)
    
class UserView(ListView):
    template_name='diary.html'
    paginate_by=30
    def get_queryset(self):
        user_id=self.kwargs['user']
        user_list=Diary.objects.filter(user=user_id).order_by('-posted_at')
        return user_list

class DetailView(DetailView):
    template_name='diary_detail.html'
    model=Diary

class redetailView(DetailView):
    def get(self, request, pk, *args, **kwargs):
        context = {}
        context["ChickPost"]=Diary.objects.filter(id=pk).first()
        context["Comment"]=DiaryGood.objects.filter(post=pk)
        return render(request,"diarygood_detail.html",context)

class DiaryMypageView(ListView):
    template_name='diary_mypage.html'
    paginate_by=30
    def get_queryset(self):
        queryset=Diary.objects.filter(user=self.request.user).order_by('-posted_at')
        return queryset

class ChickDeleteView(DeleteView):
    model=Diary
    template_name='diary_delete.html'
    success_url=reverse_lazy('diary:diary_mypage')
    def delete(self,request,*args,**kwargs):
        return super().delete(request,*args,**kwargs)

class CommentDeleteView(DeleteView):
    model=DiaryGood
    template_name='diarygood_delete.html'
    success_url=reverse_lazy('diary:diary_mypage')
    def delete(self,request,*args,**kwargs):
        return super().delete(request,*args,**kwargs)
