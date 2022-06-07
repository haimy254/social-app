# Generated by Django 4.0.4 on 2022-06-06 11:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0003_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='comment',
            field=models.ForeignKey(default='some STRING', on_delete=django.db.models.deletion.CASCADE, to='users.comments'),
        ),
        migrations.AddField(
            model_name='image',
            name='likes',
            field=models.ManyToManyField(related_name='image', to=settings.AUTH_USER_MODEL),
        ),
    ]
