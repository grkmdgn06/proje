# Generated by Django 3.0.8 on 2020-09-08 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auths', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[(None, 'Cinsiyet Seçiniz: '), ('erkek', 'ERKEK'), ('kadın', 'KADIN')], max_length=6, null=True, verbose_name='Cinsiyet'),
        ),
    ]
