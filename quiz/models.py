from django.db import models

from accounts.models import CustomUser

class Category(models.Model):
    category=models.CharField(
        verbose_name='カテゴリー',
        max_length=50,
    )
    def __str__(self):
        return self.category

class Quiz(models.Model):
    user = models.ForeignKey(
        CustomUser,
        verbose_name='ユーザー',
        on_delete=models.CASCADE,
    )
    category = models.ForeignKey(
        Category,
        verbose_name='カテゴリー',
        on_delete=models.CASCADE,
    )
    quiz = models.TextField(
        verbose_name='問題文',
    )
    answer = models.TextField(
        verbose_name='答え',
    )
    posted_at = models.DateTimeField(
        verbose_name='投稿日時',
        auto_now_add=True,
    )
    def __str__(self):
        return self.quiz