# Generated by Django 3.1.2 on 2021-06-03 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mechweb', '0131_auto_20210521_0328'),
    ]

    operations = [
        migrations.AddField(
            model_name='mechhomepage',
            name='research_profile_documentary_code',
            field=models.CharField(blank=True, max_length=264, null=True, verbose_name='Research profile documentary video code'),
        ),
    ]
