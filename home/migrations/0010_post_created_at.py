# Generated by Django 5.0.3 on 2024-06-24 13:20

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_news_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
