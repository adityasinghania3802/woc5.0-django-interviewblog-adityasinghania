# Generated by Django 4.1.5 on 2023-01-27 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0002_blogpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='job_offer_type',
            field=models.CharField(choices=[('Summer Internship', 'Summer Intership'), ('Winter Internship Only', 'Winter Intership Only'), ('Winter Intership & Job', 'Winter Internship & Job'), ('Job Only', 'Job Only')], default='None', max_length=100),
        ),
    ]
