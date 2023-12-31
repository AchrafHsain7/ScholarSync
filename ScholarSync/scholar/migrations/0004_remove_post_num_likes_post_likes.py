# Generated by Django 4.2.1 on 2023-07-09 10:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholar', '0003_alter_post_user_alter_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='num_likes',
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='user_liked_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
