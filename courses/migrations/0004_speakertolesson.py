# Generated by Django 5.1.1 on 2024-09-18 06:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_speaker_on_main_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpeakerToLesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.lesson')),
                ('speaker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.speaker')),
            ],
        ),
    ]
