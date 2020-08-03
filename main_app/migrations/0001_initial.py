# Generated by Django 3.0.8 on 2020-08-03 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('skill_type', models.CharField(choices=[('lang', 'Language'), ('frmwk', 'Framework'), ('db', 'Database'), ('styl', 'Styling')], default='lang', max_length=100, verbose_name='Skill Type')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('project_url', models.URLField(max_length=250)),
                ('description', models.TextField(max_length=500)),
                ('deployment_date', models.DateField()),
                ('skill', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='main_app.Skill')),
            ],
        ),
    ]
