# Generated by Django 3.0.8 on 2020-08-02 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('skill_type', models.CharField(choices=[('lng', 'Language'), ('frmwk', 'Framework'), ('db', 'Database'), ('styl', 'Styling')], default='lng', max_length=100, verbose_name='Skill Type')),
            ],
        ),
    ]
