from django.views import View
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView

from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import ChickPostForm,ChickCommentForm,ChickCategoryForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import ChickPost,Comment

from django.views.generic import DetailView

from django.views.generic import DeleteView

from .forms import ContactForm
from django.contrib import messages
from django.core.mail import EmailMessage
from django.views.generic import FormView

class IndexView(ListView):
    template_name="index.html"
    queryset=ChickPost.objects.order_by('-posted_at')
    paginate_by=30

@method_decorator(login_required,name='dispatch')
class CreateChickView(CreateView):
    form_class=ChickPostForm
    template_name="post_chick.html"
    success_url=reverse_lazy('chicks:post_done')
    def form_valid(self,form):
        postdata=form.save(commit=False)
        postdata.user=self.request.user
        postdata.save()
        return super().form_valid(form)

class PostSuccessView(TemplateView):
    template_name='post_success.html'

@method_decorator(login_required,name='dispatch')
class ChickCommentView(CreateView,View):
    form_class=ChickCommentForm
    template_name='post_chick_comment.html'
    success_url=reverse_lazy('chicks:post_done')
    def get(self, request, pk, *args, **kwargs):
        context = {}
        context["ChickPost"]  = ChickPost.objects.filter(id=pk).first()
        context["Comment"]  = Comment.objects.filter(post=pk)
        context["form"]     = ChickCommentForm
        return render(request,"post_chick_comment.html",context)
    def form_valid(self, form, *args, **kwargs):
        postdata=form.save(commit=False)
        postdata.comment_user=self.request.user
        postdata.save()
        return super().form_valid(form)
    
@method_decorator(login_required,name='dispatch')
class ChickCategoryView(CreateView,View):
    form_class=ChickCategoryForm
    template_name='category_post.html'
    success_url=reverse_lazy('chicks:post_done')
    def get(self, request, *args, **kwargs):
        context = {}
        context["form"]     = ChickCategoryForm
        return render(request,"category_post.html",context)
    def form_valid(self, form, *args, **kwargs):
        postdata=form.save(commit=False)
        postdata.save()
        return super().form_valid(form)

class CategoryView(ListView):
    template_name='index.html'
    paginate_by=30
    def get_queryset(self):
        category_id=self.kwargs['category']
        categories=ChickPost.objects.filter(category=category_id).order_by('-posted_at')
        return categories
    
class UserView(ListView):
    template_name='index.html'
    paginate_by=30
    def get_queryset(self):
        user_id=self.kwargs['user']
        user_list=ChickPost.objects.filter(user=user_id).order_by('-posted_at')
        return user_list

class DetailView(DetailView):
    template_name='detail.html'
    model=ChickPost

class redetailView(DetailView):
    def get(self, request, pk, *args, **kwargs):
        context = {}
        context["ChickPost"]=ChickPost.objects.filter(id=pk).first()
        context["Comment"]=Comment.objects.filter(post=pk)
        return render(request,"comment_detail.html",context)

class MypageView(ListView):
    template_name='mypage.html'
    paginate_by=30
    def get_queryset(self):
        queryset=ChickPost.objects.filter(user=self.request.user).order_by('-posted_at')
        return queryset

class ChickDeleteView(DeleteView):
    model=ChickPost
    template_name='chicks_delete.html'
    success_url=reverse_lazy('chicks:mypage')
    def delete(self,request,*args,**kwargs):
        return super().delete(request,*args,**kwargs)

class CommentDeleteView(DeleteView):
    model=Comment
    template_name='comment_delete.html'
    success_url=reverse_lazy('chicks:mypage')
    def delete(self,request,*args,**kwargs):
        return super().delete(request,*args,**kwargs)

class ContactView(FormView):
    template_name="contact.html"
    form_class=ContactForm
    success_url=reverse_lazy('chicks:contact')
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

