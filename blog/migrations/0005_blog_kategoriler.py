# Generated by Django 3.0.8 on 2020-07-16 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_kategori'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='kategoriler',
            field=models.ManyToManyField(null=True, to='blog.Kategori', verbose_name='Kategoriler'),
        ),
    ]
