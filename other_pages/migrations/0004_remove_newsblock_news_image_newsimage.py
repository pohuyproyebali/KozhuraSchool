# Generated by Django 5.1.1 on 2024-09-23 10:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('other_pages', '0003_newsblock_news_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsblock',
            name='news_image',
        ),
        migrations.CreateModel(
            name='NewsImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='other_pages.newsblock')),
            ],
        ),
    ]
