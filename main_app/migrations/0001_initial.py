# Generated by Django 3.0.8 on 2020-08-03 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='First')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last')),
                ('company', models.CharField(default='', max_length=100)),
                ('email', models.EmailField(max_length=150, verbose_name='email')),
                ('message', models.TextField(default='', max_length=500)),
                ('submition_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('skill_type', models.CharField(choices=[('lang', 'Language'), ('frmwk', 'Framework'), ('db', 'Database'), ('styl', 'Styling')], default='lang', max_length=100, verbose_name='Skill Type')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('project_url', models.URLField(max_length=250)),
                ('description', models.TextField(max_length=500)),
                ('deployment_date', models.DateField()),
                ('skill', models.ManyToManyField(to='main_app.Skill')),
            ],
        ),
    ]
