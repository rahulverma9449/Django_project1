# Generated by Django 5.0.1 on 2024-02-02 04:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0004_department_studentid_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stid', to='vege.studentid'),
        ),
    ]
