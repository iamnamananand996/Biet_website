# Generated by Django 2.2 on 2019-10-24 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PG_addmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CourseWiseSeatMatrix', models.FileField(upload_to='addmission/PG/')),
                ('notification', models.FileField(upload_to='addmission/PG/')),
                ('application_form', models.FileField(upload_to='addmission/PG/')),
                ('cut_off', models.FileField(upload_to='addmission/PG/')),
            ],
        ),
        migrations.CreateModel(
            name='UG_addmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addmission_fee', models.FileField(upload_to='addmission/UG/')),
                ('CourseWiseSeatMatrix', models.FileField(upload_to='addmission/UG/')),
                ('notification', models.FileField(upload_to='addmission/UG/')),
                ('application_form', models.FileField(upload_to='addmission/UG/')),
                ('cut_off', models.FileField(upload_to='addmission/UG/')),
            ],
        ),
    ]
