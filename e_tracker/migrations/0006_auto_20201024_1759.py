# Generated by Django 3.1.2 on 2020-10-24 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('e_tracker', '0005_auto_20201023_0854'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='profile',
        ),
        migrations.AddField(
            model_name='expense',
            name='user',
            field=models.ForeignKey(default=18, on_delete=django.db.models.deletion.CASCADE, to='e_tracker.profile'),
        ),
    ]
