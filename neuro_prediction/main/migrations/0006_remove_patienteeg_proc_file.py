# Generated by Django 5.0.3 on 2024-05-08 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_patienteeg_proc_file_alter_patienteeg_raw_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patienteeg',
            name='proc_file',
        ),
    ]