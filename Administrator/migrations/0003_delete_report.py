# Generated by Django 5.0.4 on 2024-07-04 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Administrator', '0002_remove_administrator_status_administrator_is_active_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Report',
        ),
    ]
