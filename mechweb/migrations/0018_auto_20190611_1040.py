# Generated by Django 2.2.1 on 2019-06-11 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mechweb', '0017_auto_20190611_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnuspage',
            name='programme',
            field=models.CharField(choices=[('0', 'Bachelor'), ('1', 'Masters'), ('2', 'Research Scholar'), ('3', 'Other')], max_length=2),
        ),
        migrations.AlterField(
            model_name='coursepage',
            name='document',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.Document', verbose_name='Syllabus'),
        ),
        migrations.AlterField(
            model_name='coursepage',
            name='eligible_programmes',
            field=models.CharField(choices=[('0', 'Bachelor'), ('1', 'Masters'), ('2', 'Research Scholar'), ('3', 'Other')], default='0', help_text='Minimum qualification needed to take course', max_length=100),
        ),
        migrations.AlterField(
            model_name='staffpage',
            name='designation',
            field=models.CharField(choices=[('0', 'Administrative Staff'), ('1', 'Lab Staff'), ('2', 'Technicial staff'), ('3', 'PostDoc'), ('4', 'Others')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='studentpage',
            name='programme',
            field=models.CharField(choices=[('0', 'Bachelor'), ('1', 'Masters'), ('2', 'Research Scholar'), ('3', 'Other')], max_length=2),
        ),
    ]
