# Generated by Django 5.1b1 on 2024-07-19 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_alter_task_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_verified',
            field=models.BooleanField(default=False),
        ),
    ]