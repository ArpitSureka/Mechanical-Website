# Generated by Django 2.2.1 on 2020-02-10 10:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mechweb', '0089_auto_20200210_0741'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursepage',
            name='seven',
            field=models.BooleanField(default=False, verbose_name='PG Electives'),
        ),
        migrations.AddField(
            model_name='coursepage',
            name='seven_sem',
            field=models.IntegerField(blank=True, default=0, verbose_name='Semester'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='alumnuspage',
            name='leaving_year',
            field=models.DateField(default=datetime.datetime(2024, 2, 9, 10, 31, 52, 851710, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='committeepage',
            name='tenure_end',
            field=models.DateField(default=datetime.datetime(2021, 2, 9, 10, 31, 52, 873068, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='studentpage',
            name='leaving_year',
            field=models.DateField(default=datetime.datetime(2024, 2, 9, 10, 31, 52, 851710, tzinfo=utc)),
        ),
    ]
