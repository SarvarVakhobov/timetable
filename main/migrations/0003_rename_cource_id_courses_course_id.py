# Generated by Django 4.0.4 on 2022-05-18 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_courses_cource_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courses',
            old_name='cource_id',
            new_name='course_id',
        ),
    ]