# Generated by Django 5.0.3 on 2024-05-08 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_patient_first_name_patient_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patienteeg',
            name='proc_file',
            field=models.FileField(upload_to='proc_eeg'),
        ),
        migrations.AlterField(
            model_name='patienteeg',
            name='raw_file',
            field=models.FileField(upload_to='raw_eeg'),
        ),
    ]