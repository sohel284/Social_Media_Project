# Generated by Django 3.2.3 on 2021-05-25 02:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post',
            new_name='post_author',
        ),
    ]
