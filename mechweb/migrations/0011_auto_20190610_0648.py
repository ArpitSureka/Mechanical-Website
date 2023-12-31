# Generated by Django 2.2.1 on 2019-06-10 06:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mechweb', '0010_auto_20190610_0641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnuspage',
            name='enrolment_year',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='coursepagefaculty',
            name='session',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Instruction start date'),
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='facultyaward',
            name='award_time',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='staffpage',
            name='joining_year',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='studentpage',
            name='enrolment_year',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
