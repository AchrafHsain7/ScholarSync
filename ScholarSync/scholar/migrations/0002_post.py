# Generated by Django 4.2.1 on 2023-07-08 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scholar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('num_likes', models.PositiveIntegerField(default=0)),
                ('image', models.URLField()),
                ('description', models.CharField(blank=True, max_length=200)),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_posts', to='scholar.profile')),
            ],
        ),
    ]
