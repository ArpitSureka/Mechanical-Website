# Generated by Django 2.2.1 on 2019-06-08 11:39

from django.db import migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mechweb', '0003_auto_20190608_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentpagelink',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='stud_links', to='mechweb.StudentPage'),
        ),
    ]
