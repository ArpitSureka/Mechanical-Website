# Generated by Django 2.2.1 on 2020-02-09 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mechweb', '0076_auto_20200209_0618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='award_title',
            field=models.CharField(max_length=500),
        ),
    ]
