# Generated by Django 3.2.8 on 2022-03-03 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='lat',
            field=models.CharField(blank=True, default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='event',
            name='lng',
            field=models.CharField(blank=True, default=None, max_length=50),
        ),
    ]
