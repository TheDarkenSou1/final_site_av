# Generated by Django 4.1.4 on 2022-12-30 17:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercontact',
            name='email',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(message='Некоректно введено пошту.', regex='^[a-zA-Z0-9](-?[a-zA-Z0-9_])+@[a-zA-Z0-9]+(\\.[a-zA-Z0-9]+)*$')]),
        ),
    ]
