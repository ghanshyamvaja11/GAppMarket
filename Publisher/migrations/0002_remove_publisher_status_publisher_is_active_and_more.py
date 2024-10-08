# Generated by Django 5.0.4 on 2024-07-01 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Publisher', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publisher',
            name='status',
        ),
        migrations.AddField(
            model_name='publisher',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='publisher',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='publisher',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='email',
            field=models.EmailField(max_length=255, unique=True, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
