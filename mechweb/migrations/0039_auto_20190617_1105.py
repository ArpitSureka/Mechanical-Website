# Generated by Django 2.2.1 on 2019-06-17 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mechweb', '0038_auto_20190617_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicationpage',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='publicationpage',
            name='pub_type',
            field=models.CharField(choices=[('0', 'Journal Publication'), ('1', 'Conference Publication'), ('2', 'Patent'), ('3', 'Books'), ('4', 'Book Chapters'), ('5', 'Poster')], default='0', max_length=2),
        ),
    ]
