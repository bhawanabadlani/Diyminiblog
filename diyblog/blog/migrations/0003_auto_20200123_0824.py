# Generated by Django 2.2.9 on 2020-01-23 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200123_0659'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='date_of_death',
            field=models.DateField(blank=True, null=True),
        ),
    ]
