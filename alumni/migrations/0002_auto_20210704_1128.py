# Generated by Django 3.1.2 on 2021-07-04 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpageurl',
            name='url',
            field=models.URLField(max_length=2083),
        ),
    ]
