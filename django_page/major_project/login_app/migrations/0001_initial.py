# Generated by Django 5.1.4 on 2024-12-11 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_image', models.ImageField(upload_to='')),
                ('doctor_name', models.CharField(max_length=100)),
                ('doctor_details', models.CharField(max_length=1000)),
            ],
        ),
    ]
