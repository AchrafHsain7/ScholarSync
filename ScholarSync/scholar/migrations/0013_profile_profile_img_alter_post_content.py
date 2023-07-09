# Generated by Django 4.2.1 on 2023-07-09 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholar', '0012_post_favorite_of_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_img',
            field=models.URLField(default='https://img.freepik.com/free-icon/user_318-414374.jpg?size=626&ext=jpg&ga=GA1.2.1896589579.1688924061&semt=ais'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.CharField(max_length=2000),
        ),
    ]
