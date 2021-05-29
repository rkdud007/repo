# Generated by Django 3.2.3 on 2021-05-29 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oftoday', '0005_auto_20210530_0040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like_ootd',
            name='ootd',
        ),
        migrations.RemoveField(
            model_name='like_ootd',
            name='user',
        ),
        migrations.RemoveField(
            model_name='fotd',
            name='day',
        ),
        migrations.RemoveField(
            model_name='fotd',
            name='share',
        ),
        migrations.RemoveField(
            model_name='fotd',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='fotd',
            name='time',
        ),
        migrations.RemoveField(
            model_name='motd',
            name='day',
        ),
        migrations.RemoveField(
            model_name='ootd',
            name='day',
        ),
        migrations.RemoveField(
            model_name='ootd',
            name='share',
        ),
        migrations.RemoveField(
            model_name='ootd',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='ootd',
            name='time',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
        migrations.RemoveField(
            model_name='totd',
            name='day',
        ),
        migrations.RemoveField(
            model_name='totd',
            name='time',
        ),
        migrations.DeleteModel(
            name='Like_Fotd',
        ),
        migrations.DeleteModel(
            name='Like_Ootd',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
