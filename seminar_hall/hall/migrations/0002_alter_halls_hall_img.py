# Generated by Django 5.0.1 on 2024-02-03 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hall', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='halls',
            name='hall_img',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
