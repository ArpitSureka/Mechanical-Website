# Generated by Django 3.1.2 on 2021-01-16 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('mechweb', '0119_newsannouncementhomepage_newsannouncementpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsannouncementpage',
            name='photo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.DeleteModel(
            name='HomeTextPanel',
        ),
    ]
