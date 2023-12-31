# Generated by Django 2.2.1 on 2019-06-17 13:11

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mechweb', '0039_auto_20190617_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicationpage',
            name='name',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='publicationpage',
            name='pub_issue',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='publicationpage',
            name='pub_journal',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='publicationpage',
            name='pub_vol',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.CreateModel(
            name='ResearchLabPostdocs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('research_statement', wagtail.core.fields.RichTextField(blank=True)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='postdocs', to='mechweb.ResearchLabPage')),
                ('postdoc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='postdoc_lab', to='mechweb.StaffPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
