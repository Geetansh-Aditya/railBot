# Generated by Django 5.1 on 2024-08-17 11:19

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_alter_complaint_client_pnr'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='complaint_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
