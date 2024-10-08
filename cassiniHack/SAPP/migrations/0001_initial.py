# Generated by Django 3.2.25 on 2024-09-14 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegionalInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('month', models.PositiveIntegerField()),
                ('year', models.PositiveIntegerField()),
                ('min_temp', models.FloatField()),
                ('max_temp', models.FloatField()),
                ('avg_temp', models.FloatField()),
                ('total_perception', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Seeds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('min_temp', models.FloatField()),
                ('max_temp', models.FloatField()),
                ('min_rainfall', models.FloatField()),
                ('max_rainfall', models.FloatField()),
                ('min_ph_soil', models.FloatField()),
                ('max_ph_soil', models.FloatField()),
            ],
        ),
    ]
