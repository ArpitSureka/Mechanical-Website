# Generated by Django 2.2.9 on 2020-02-12 09:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mechweb', '0102_auto_20200212_0843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnuspage',
            name='leaving_year',
            field=models.DateField(default=datetime.datetime(2024, 2, 11, 9, 43, 5, 234484, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='committeepage',
            name='tenure_end',
            field=models.DateField(default=datetime.datetime(2021, 2, 11, 9, 43, 5, 256309, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='studentpage',
            name='leaving_year',
            field=models.DateField(default=datetime.datetime(2024, 2, 11, 9, 43, 5, 234484, tzinfo=utc)),
        ),
    ]
