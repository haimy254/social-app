# Generated by Django 4.0.4 on 2022-06-10 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_image_user_alter_profile_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile_photo',
            new_name='avatar',
        ),
    ]
