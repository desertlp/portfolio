# Generated by Django 3.0.8 on 2020-08-03 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='skill',
            new_name='skills',
        ),
    ]
