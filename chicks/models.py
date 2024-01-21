from django.db import models
from accounts.models import CustomUser

class Category(models.Model):
    title = models.CharField(
        verbose_name='カテゴリ',
        max_length=30,
    )
    def __str__(self):
        return self.title

class ChickPost(models.Model):
    user = models.ForeignKey(
        CustomUser,
        verbose_name='ユーザー',
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category,
        verbose_name='カテゴリ',
        on_delete=models.PROTECT
    )
    title = models.CharField(
        verbose_name='タイトル',
        max_length=50,
    )
    comment = models.TextField(
        verbose_name='コメント',
    )
    image = models.ImageField(
        verbose_name='画像',
        upload_to='images',
        blank=True,
        null=True
    )
    posted_at = models.DateTimeField(
        verbose_name='投稿日時',
        auto_now_add=True,
    )
    def __str__(self):
        return self.title

class Comment(models.Model):
    comment_user = models.ForeignKey(
        CustomUser,
        verbose_name='ユーザー',
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(
        ChickPost,
        verbose_name='投稿',
        on_delete=models.CASCADE,
        related_name='comments',
    )
    thoughts_on_comment = models.TextField(
        verbose_name='コメントへの感想',
    )
    comment_image = models.ImageField(
        verbose_name='画像',
        upload_to='images',
        blank=True,
        null=True,
    )
    posted_at = models.DateTimeField(
        verbose_name='投稿日時',
        auto_now_add=True,
    )
    def __str__(self):
        return self.thoughts_on_comment