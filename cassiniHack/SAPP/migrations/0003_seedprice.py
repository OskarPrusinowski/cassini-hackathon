# Generated by Django 4.2.7 on 2024-09-15 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SAPP', '0002_soil'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeedPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('seed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='SAPP.seeds')),
            ],
        ),
    ]
