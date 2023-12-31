# Generated by Django 3.1.2 on 2021-12-18 14:39

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('mechweb', '0138_customlink_footercolumn'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='facultyhomepage',
            options={'verbose_name': 'Faculty Home'},
        ),
        migrations.RemoveField(
            model_name='mechhomepage',
            name='HOD_image',
        ),
        migrations.RemoveField(
            model_name='mechhomepage',
            name='HOD_message',
        ),
        migrations.AddField(
            model_name='aboutiitgmech',
            name='HOD_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='aboutiitgmech',
            name='HOD_message',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]
