# Generated by Django 3.1.2 on 2020-10-22 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('e_tracker', '0002_expense_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='expense', to='e_tracker.profile'),
        ),
    ]
