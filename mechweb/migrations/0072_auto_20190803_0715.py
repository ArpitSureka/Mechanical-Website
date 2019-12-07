# Generated by Django 2.2.1 on 2019-08-03 07:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mechweb', '0071_facultypreviouswork'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facultypage',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='faculty', to=settings.AUTH_USER_MODEL),
        ),
    ]
