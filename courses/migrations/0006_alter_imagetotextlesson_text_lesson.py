# Generated by Django 5.1.1 on 2024-09-23 07:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_alter_answertotext_text_alter_lessontouser_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagetotextlesson',
            name='text_lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_to_text_lesson', to='courses.texttolesson'),
        ),
    ]
