# Generated by Django 4.0.4 on 2022-05-18 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_cource_id_courses_course_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='course',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='course', serialize=False, to='main.courses'),
        ),
    ]
