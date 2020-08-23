# Generated by Django 3.1 on 2020-08-23 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20200823_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('todo', 'Todo'), ('in_progress', 'In Progress'), ('done', 'Done')], default='todo', max_length=255),
        ),
    ]
