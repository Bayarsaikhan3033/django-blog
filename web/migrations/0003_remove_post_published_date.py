# Generated by Django 3.0.4 on 2020-03-04 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_comment_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='published_date',
        ),
    ]
