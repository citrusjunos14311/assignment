# Generated by Django 4.0.2 on 2024-01-09 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chicks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=30, verbose_name='カテゴリ'),
        ),
        migrations.AlterField(
            model_name='chickpost',
            name='title',
            field=models.CharField(max_length=50, verbose_name='タイトル'),
        ),
    ]
