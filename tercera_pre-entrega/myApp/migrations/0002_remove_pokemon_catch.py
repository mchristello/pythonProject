# Generated by Django 4.2.5 on 2023-09-21 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='catch',
        ),
    ]