# Generated by Django 2.2.1 on 2020-02-09 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mechweb', '0077_auto_20200209_0620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='conferrer',
            field=models.CharField(max_length=200),
        ),
    ]
