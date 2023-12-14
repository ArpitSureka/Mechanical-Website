# Generated by Django 3.1.1 on 2020-09-29 14:46

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mechweb', '0108_auto_20200923_1153'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResearchLabTechStaff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('responsibilities', wagtail.core.fields.RichTextField(blank=True)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='researchlabpage',
            name='scientific_officer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='scientific_officer', to='mechweb.staffpage'),
        ),
        migrations.DeleteModel(
            name='ResearchLabPostdocs',
        ),
        migrations.AddField(
            model_name='researchlabtechstaff',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tech_staffs', to='mechweb.researchlabpage'),
        ),
        migrations.AddField(
            model_name='researchlabtechstaff',
            name='tech_staff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tech_staff_lab', to='mechweb.staffpage'),
        ),
    ]
