# Generated by Django 5.0.1 on 2024-02-03 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='halls',
            fields=[
                ('hall_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('hall_img', models.ImageField(upload_to='')),
                ('hall_name', models.CharField(max_length=50)),
                ('hall_mrp', models.IntegerField()),
            ],
        ),
    ]