# Generated by Django 2.2.1 on 2020-02-11 13:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mechweb', '0098_auto_20200210_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicationpage',
            name='alt_detail_text',
            field=models.CharField(blank=True, help_text='Add any other type of data, like ISBN number, publisher etc', max_length=1000),
        ),
        migrations.AlterField(
            model_name='alumnuspage',
            name='leaving_year',
            field=models.DateField(default=datetime.datetime(2024, 2, 10, 13, 49, 31, 435079, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='committeepage',
            name='tenure_end',
            field=models.DateField(default=datetime.datetime(2021, 2, 10, 13, 49, 31, 457126, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(default=True, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
        migrations.AlterField(
            model_name='staffpage',
            name='designation',
            field=models.CharField(choices=[('4', 'Technical Superintendent'), ('0', 'Jr. Assistant'), ('1', 'Jr. Superintendent'), ('2', 'Jr. Technical Superintendent'), ('3', 'Jr. Technician'), ('6', 'Technical Officer Gr I'), ('5', 'Technical Officer Gr II'), ('7', 'Junior Technical Officer'), ('8', 'Asst. Workshop Superintendent'), ('9', 'PostDoc'), ('10', 'Others')], default='10', max_length=2),
        ),
        migrations.AlterField(
            model_name='studentpage',
            name='leaving_year',
            field=models.DateField(default=datetime.datetime(2024, 2, 10, 13, 49, 31, 435079, tzinfo=utc)),
        ),
    ]
