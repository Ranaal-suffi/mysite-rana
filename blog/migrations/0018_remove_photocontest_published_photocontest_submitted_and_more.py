# Generated by Django 4.1.1 on 2022-11-29 13:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_photocontest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photocontest',
            name='published',
        ),
        migrations.AddField(
            model_name='photocontest',
            name='submitted',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='submitted',
            field=models.DateTimeField(blank=True, help_text='The date & time this artiicle was published', null=True),
        ),
    ]
