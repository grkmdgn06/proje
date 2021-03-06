# Generated by Django 3.0.8 on 2020-08-16 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_remove_blog_content1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(blank=True, max_length=50, null=True, verbose_name='İsim')),
                ('soyisim', models.CharField(blank=True, max_length=50, null=True, verbose_name='Soyisim')),
                ('email', models.EmailField(help_text='Bu alan boş bırakılamaz..', max_length=254, null=True, verbose_name='e-mail')),
                ('icerik', models.CharField(help_text='Firinizi yazınız..', max_length=1000, null=True, verbose_name='Yorum')),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('blog', models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Blog')),
            ],
            options={
                'verbose_name_plural': 'Yorumlar',
            },
        ),
    ]
