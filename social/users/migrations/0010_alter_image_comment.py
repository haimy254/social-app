# Generated by Django 4.0.4 on 2022-06-06 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_image_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='comment',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.comments'),
        ),
    ]