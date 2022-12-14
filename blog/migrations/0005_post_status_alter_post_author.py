"""missing"""
# Generated by Django 4.1.1 on 2022-10-10 00:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    """missing"""
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_alter_post_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'draft'), ('published', 'published')],
            default='draft', help_text='Set to "published" to make this post pblicly visible',\
                max_length=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.
            PROTECT, related_name='blog_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
