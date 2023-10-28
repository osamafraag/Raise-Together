# Generated by Django 3.2.12 on 2023-10-28 00:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('donations', '0002_remove_donation_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='donator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='donations', to=settings.AUTH_USER_MODEL),
        ),
    ]
