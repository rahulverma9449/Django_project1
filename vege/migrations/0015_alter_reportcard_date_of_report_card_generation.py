# Generated by Django 5.0.1 on 2024-02-18 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0014_alter_subjectmarks_unique_together_reportcard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportcard',
            name='date_of_report_card_generation',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
