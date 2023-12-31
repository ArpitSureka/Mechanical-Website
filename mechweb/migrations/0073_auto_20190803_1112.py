# Generated by Django 2.2.1 on 2019-08-03 11:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('mechweb', '0072_auto_20190803_0715'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectPageFacultyCoPI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('project_statement', wagtail.core.fields.RichTextField(blank=True)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProjectPageFacultyPI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('project_statement', wagtail.core.fields.RichTextField(blank=True)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProjectPageOtherInvestigator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('name', models.CharField(max_length=100)),
                ('organization', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='projectpagestudent',
            name='page',
        ),
        migrations.RemoveField(
            model_name='projectpagestudent',
            name='student',
        ),
        migrations.RemoveField(
            model_name='projectpage',
            name='principal_investigator',
        ),
        migrations.AddField(
            model_name='categories',
            name='photo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='mechhomepage',
            name='HOD_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='mechhomepage',
            name='donate_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='mechhomepage',
            name='donate_message',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='mechhomepage',
            name='donation_link',
            field=models.URLField(default='http://www.iitg.ac.in/epay', max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aboutiitgmech',
            name='about',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='aboutiitgmech',
            name='history',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='aboutiitgmech',
            name='vision',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='facultypage',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='faculty', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='projectpage',
            name='name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='publicationpage',
            name='alt_people_text',
            field=models.CharField(blank=True, help_text='Add the exact sequence of names as in the publication', max_length=1000),
        ),
        migrations.DeleteModel(
            name='ProjectPageFaculty',
        ),
        migrations.DeleteModel(
            name='ProjectPageStudent',
        ),
        migrations.AddField(
            model_name='projectpageotherinvestigator',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='oi', to='mechweb.ProjectPage'),
        ),
        migrations.AddField(
            model_name='projectpagefacultypi',
            name='faculty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pi', to='mechweb.FacultyPage'),
        ),
        migrations.AddField(
            model_name='projectpagefacultypi',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='faculty_pi', to='mechweb.ProjectPage'),
        ),
        migrations.AddField(
            model_name='projectpagefacultycopi',
            name='faculty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='copi', to='mechweb.FacultyPage'),
        ),
        migrations.AddField(
            model_name='projectpagefacultycopi',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='faculty_copi', to='mechweb.ProjectPage'),
        ),
    ]
