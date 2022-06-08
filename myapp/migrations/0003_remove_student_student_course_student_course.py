# Generated by Django 4.0.5 on 2022-06-08 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_course_student_student_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='student_course',
        ),
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_course', to='myapp.course'),
        ),
    ]
