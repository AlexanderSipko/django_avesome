# Generated by Django 4.0.3 on 2022-03-08 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='upload',
            field=models.FileField(blank=True, upload_to='uploads/%Y/%m/%d/'),
        ),
    ]
