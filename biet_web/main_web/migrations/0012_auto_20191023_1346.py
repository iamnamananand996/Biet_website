# Generated by Django 2.2 on 2019-10-23 08:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_web', '0011_auto_20191023_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallary',
            name='images',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='main_gallary'),
            preserve_default=False,
        ),
    ]
