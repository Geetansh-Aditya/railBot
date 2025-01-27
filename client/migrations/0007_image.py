# Generated by Django 5.1 on 2024-08-18 11:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0006_alter_complaint_client_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_pnr', models.CharField(max_length=10, unique=True, validators=[django.core.validators.MinLengthValidator(10)])),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
