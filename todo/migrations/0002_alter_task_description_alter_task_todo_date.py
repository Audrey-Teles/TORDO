# Generated by Django 4.1.6 on 2023-02-05 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='todo_date',
            field=models.DateField(null=True),
        ),
    ]
