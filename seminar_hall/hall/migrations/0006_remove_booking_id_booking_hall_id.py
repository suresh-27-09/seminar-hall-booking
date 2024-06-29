# Generated by Django 5.0.1 on 2024-02-08 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hall', '0005_booking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='id',
        ),
        migrations.AddField(
            model_name='booking',
            name='hall_id',
            field=models.BigAutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]