# Generated by Django 4.1.5 on 2023-02-06 09:14

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0013_blogpost_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='blog_content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]