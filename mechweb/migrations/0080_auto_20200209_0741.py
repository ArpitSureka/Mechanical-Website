# Generated by Django 2.2.1 on 2020-02-09 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mechweb', '0079_auto_20200209_0739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facultypage',
            name='leaving_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
