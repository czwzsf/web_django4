# Generated by Django 4.0 on 2022-06-06 02:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_task_createtime'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Task',
        ),
    ]
