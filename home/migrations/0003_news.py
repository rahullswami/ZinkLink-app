# Generated by Django 5.0.3 on 2024-06-23 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_user_bio_zink_user_profile_bio_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('sub_heading', models.CharField(max_length=100)),
                ('news', models.TextField()),
            ],
        ),
    ]
