# Generated by Django 3.1.5 on 2021-01-19 04:29

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_blog_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
