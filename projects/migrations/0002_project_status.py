# Generated by Django 4.2.6 on 2023-10-28 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Canceled', 'Canceled'), ('Completed', 'Completed')], default='Active', max_length=20),
        ),
    ]
