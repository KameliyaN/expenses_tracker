# Generated by Django 3.1.2 on 2020-10-26 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('e_tracker', '0007_auto_20201024_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='expense',
            name='user',
            field=models.ForeignKey(default=28, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='e_tracker.profile'),
        ),
    ]