# Generated by Django 4.2.6 on 2024-06-27 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hall', '0007_remove_booking_hall_id_booking_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='uname',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
