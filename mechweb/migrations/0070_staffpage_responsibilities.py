# Generated by Django 2.2.1 on 2019-07-20 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mechweb', '0069_auto_20190720_0743'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffpage',
            name='responsibilities',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
