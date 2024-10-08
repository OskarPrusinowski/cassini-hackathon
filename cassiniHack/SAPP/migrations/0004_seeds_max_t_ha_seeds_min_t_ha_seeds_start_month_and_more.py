# Generated by Django 4.2.7 on 2024-09-15 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SAPP', '0003_seedprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='seeds',
            name='max_t_ha',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='seeds',
            name='min_t_ha',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='seeds',
            name='start_month',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='seeds',
            name='stop_month',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
