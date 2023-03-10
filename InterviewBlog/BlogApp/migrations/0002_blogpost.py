# Generated by Django 4.1.5 on 2023-01-27 06:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BlogApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('blog_title', models.CharField(default='Read my first post', max_length=100)),
                ('blog_content', models.CharField(default='..', max_length=500)),
                ('company_name', models.CharField(default='', max_length=50)),
                ('job_offer_type', models.CharField(choices=[('Summer Internship', 'Summer Intership'), ('Winter Internship Only', 'Winter Intership Only'), ('Winter Intership & Job', 'Winter Internship & Job'), ('Job Only', 'Job Only')], max_length=50)),
                ('job_profile', models.CharField(default='', max_length=50)),
                ('year', models.IntegerField()),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
