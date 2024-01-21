from django.urls import path
from . import views
app_name='chicks'

urlpatterns=[
    path('',views.IndexView.as_view(),name='index'),
    path('post/',views.CreateChickView.as_view(),name='post'),
    path('post_done/',views.PostSuccessView.as_view(),name='post_done'),
    path('chicks/<int:category>',views.CategoryView.as_view(),name='chicks_cat'),
    path('user-list/<int:user>',views.UserView.as_view(),name='user_list'),
    path('chicks-detail/<int:pk>',views.DetailView.as_view(),name='chicks_detail'),
    path('mypage/',views.MypageView.as_view(),name='mypage'),
    path('chicks/<int:pk>/delete/',views.ChickDeleteView.as_view(),name='chicks_delete'),
    path('comment/<int:pk>/delete/',views.CommentDeleteView.as_view(),name='comment_delete'),
    path('contact/',views.ContactView.as_view(),name="contact"),
    path('comment_detail/<int:pk>',views.redetailView.as_view(),name='comment_detail'),
    path('comment_post/<int:pk>/',views.ChickCommentView.as_view(),name='comment_post'),
    path('category_post/',views.ChickCategoryView.as_view(),name='category_post')
]