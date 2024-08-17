# Generated by Django 5.1 on 2024-08-16 22:25

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_rename_reporter_issue_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='date_reported',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='register',
            name='campus',
            field=models.CharField(choices=[('C1', 'Campus 1'), ('C2', 'Campus 2')], default=1, max_length=20, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='issue',
            name='fault_detection',
            field=models.TextField(max_length=500, unique=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='department',
            field=models.CharField(choices=[('EW', 'Estate and works'), ('AD', 'Admin block'), ('ST', 'Student Affairs'), ('RG', 'Registry'), ('TH', 'Theatre Hall'), ('BS', 'Bursary'), ('LB', 'Library'), ('PP', 'Physical Planning'), ('PD', 'Physics DP'), ('CH', 'Chemistry DP'), ('PL', 'Physics Lab'), ('CL', 'Chemistry Lab')], max_length=100, unique=True),
        ),
    ]
