# Generated by Django 3.0.8 on 2020-08-21 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item_display', '0007_auto_20200821_0358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wash_basin',
            name='item_image1',
        ),
        migrations.AddField(
            model_name='wash_basin',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
