# Generated by Django 3.0.8 on 2020-08-16 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20200816_2057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='content1',
        ),
    ]
