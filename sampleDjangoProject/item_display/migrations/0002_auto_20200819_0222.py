# Generated by Django 3.0.8 on 2020-08-19 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item_display', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wash_basin',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
    ]