# Generated by Django 4.2.3 on 2024-06-23 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(help_text='Enter the Task ', max_length=50)),
                ('des', models.CharField(help_text='Enter the Description', max_length=200)),
            ],
        ),
    ]
