# Generated by Django 3.1.2 on 2020-10-17 19:04

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mechweb', '0111_auto_20201012_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labequipment',
            name='specifications',
            field=wagtail.core.fields.RichTextField(blank=True, verbose_name='Description'),
        ),
    ]
