# Generated by Django 4.1.1 on 2022-12-19 01:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_remove_photocontest_published_photocontest_submitted_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='approved',
            field=models.BooleanField(default=True),
        ),
    ]
