# Generated by Django 2.2.1 on 2020-02-09 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mechweb', '0075_auto_20191209_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='award_title',
            field=models.CharField(max_length=100),
        ),
    ]
