# Generated by Django 5.1 on 2024-08-26 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_alter_issue_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='staff',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
