# Generated by Django 3.1.2 on 2020-10-23 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('e_tracker', '0004_auto_20201022_1316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='user',
            new_name='profile',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
    ]
