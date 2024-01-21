from django.urls import path
from . import views
app_name='diary'

urlpatterns=[
    path('',views.DiaryIndexView.as_view(),name='diary'),
    path('post/',views.CreateChickView.as_view(),name='post'),
    path('post_done/',views.PostSuccessView.as_view(),name='post_done'),
    #path('chicks/<int:category>',views.CategoryView.as_view(),name='chicks_cat'),
    path('user-list/<int:user>',views.UserView.as_view(),name='user_list'),
    path('diary-detail/<int:pk>',views.DetailView.as_view(),name='diary_detail'),
    path('diary_mypage/',views.DiaryMypageView.as_view(),name='diary_mypage'),
    path('diary/<int:pk>/delete/',views.ChickDeleteView.as_view(),name='diary_delete'),
    path('diarygood/<int:pk>/delete/',views.CommentDeleteView.as_view(),name='diarygood_delete'),
    path('diarygood_detail/<int:pk>',views.redetailView.as_view(),name='diarygood_detail'),
    path('diarygood_post/<int:pk>/',views.ChickCommentView.as_view(),name='diarygood_post'),
    #path('category_post/',views.ChickCategoryView.as_view(),name='category_post')
]