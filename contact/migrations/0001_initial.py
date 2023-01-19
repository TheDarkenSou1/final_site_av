# Generated by Django 4.1.4 on 2022-12-30 14:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=80, validators=[django.core.validators.RegexValidator(message='Некоректно введено пошту.', regex='^[a-zA-Z0-9](-?[a-zA-Z0-9_])+@[a-zA-Z0-9]+(\\.[a-zA-Z0-9]+)*$')])),
                ('subject', models.CharField(max_length=50)),
                ('message', models.TextField(max_length=500)),
                ('is_processed', models.BooleanField(default=False)),
                ('data_in', models.DateTimeField(auto_now_add=True)),
                ('date_modify', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-data_in',),
            },
        ),
    ]