# Generated by Django 4.1.5 on 2023-02-04 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0010_remove_blogpost_likecount'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
