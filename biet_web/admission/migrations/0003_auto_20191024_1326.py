# Generated by Django 2.2 on 2019-10-24 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0002_auto_20191024_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pg_addmission',
            name='cut_off',
            field=models.FileField(blank=True, upload_to='addmission/PG/'),
        ),
        migrations.AlterField(
            model_name='pg_addmission',
            name='notification',
            field=models.FileField(blank=True, upload_to='addmission/PG/'),
        ),
    ]
