# Generated by Django 5.0.3 on 2024-07-08 18:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="O número de telefone deve estar no formato: '+999999999'. Até 15 dígitos permitidos.", regex='^\\+?1?\\d{9,15}$')])),
            ],
        ),
    ]
