# Generated by Django 5.0.4 on 2024-07-02 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_purchase'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]
