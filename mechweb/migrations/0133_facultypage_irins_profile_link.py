# Generated by Django 3.1.2 on 2021-06-05 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mechweb', '0132_mechhomepage_research_profile_documentary_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='facultypage',
            name='irins_profile_link',
            field=models.URLField(blank=True, max_length=2000),
        ),
    ]
