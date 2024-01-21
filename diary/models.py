from django.db import models

from accounts.models import CustomUser

class Diary(models.Model):
    user = models.ForeignKey(
        CustomUser,
        verbose_name='ユーザー',
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        verbose_name='タイトル',
        max_length=100,
    )
    sentence = models.TextField(
        verbose_name='文章',
    )
    posted_at = models.DateTimeField(
        verbose_name='投稿日時',
        auto_now_add=True,
    )
    def __str__(self):
        return self.title

class DiaryGood(models.Model):
    good_user= models.ForeignKey(
        CustomUser,
        verbose_name='ユーザー',
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(
        Diary,
        verbose_name='投稿',
        on_delete=models.CASCADE,
    )
    posted_at = models.DateTimeField(
        verbose_name='投稿日時',
        auto_now_add=True,
    )
    def __int__(self):
        return self.post
