# Generated by Django 4.2.14 on 2024-07-24 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image_name',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.FileField(null=True, upload_to='posts'),
        ),
    ]
