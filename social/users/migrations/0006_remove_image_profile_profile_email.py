# Generated by Django 4.0.4 on 2023-06-14 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_profile_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='profile',
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=30, null=True),
        ),
    ]