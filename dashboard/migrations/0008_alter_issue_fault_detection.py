# Generated by Django 5.1 on 2024-08-26 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_alter_issue_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='fault_detection',
            field=models.TextField(max_length=450, null=True),
        ),
    ]
