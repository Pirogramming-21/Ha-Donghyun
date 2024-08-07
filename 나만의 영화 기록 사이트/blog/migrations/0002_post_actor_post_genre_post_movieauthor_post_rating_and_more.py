# Generated by Django 4.2.13 on 2024-07-12 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='actor',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='post',
            name='genre',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='post',
            name='movieauthor',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='post',
            name='rating',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='post',
            name='running_time',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
    ]
