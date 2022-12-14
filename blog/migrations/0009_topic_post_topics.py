"""missing"""
# Generated by Django 4.1.1 on 2022-10-14 17:07

from django.db import migrations, models


class Migration(migrations.Migration):
    """missing"""
    dependencies = [
        ('blog', '0008_alter_post_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,\
                serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='topics',
            field=models.ManyToManyField(related_name='blog_posts', to='blog.topic'),
        ),
    ]
