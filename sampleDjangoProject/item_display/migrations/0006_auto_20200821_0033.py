# Generated by Django 3.0.8 on 2020-08-21 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item_display', '0005_wash_basin_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wash_basin',
            name='item_name',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]