# Generated by Django 4.1.5 on 2023-02-06 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0017_remove_comment_name_comment_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='likecount',
            field=models.IntegerField(default=0),
        ),
    ]