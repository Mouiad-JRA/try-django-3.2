# Generated by Django 4.0.4 on 2022-05-25 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='Title',
            new_name='title',
        ),
    ]
