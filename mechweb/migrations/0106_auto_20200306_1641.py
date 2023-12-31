# Generated by Django 2.2.10 on 2020-03-06 16:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mechweb', '0105_auto_20200306_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnuspage',
            name='leaving_year',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='committeepage',
            name='tenure_end',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='studentpage',
            name='leaving_year',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
