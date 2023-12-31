# Generated by Django 5.0 on 2023-12-13 06:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UnitMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemCode', models.CharField(max_length=6)),
                ('ItemName', models.CharField(max_length=30)),
                ('ItemDesc', models.CharField(max_length=100)),
                ('Type', models.CharField(max_length=10)),
                ('Make', models.CharField(max_length=30)),
                ('category', models.CharField(max_length=100)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.unitmaster')),
            ],
        ),
    ]
