# Generated by Django 2.0.3 on 2018-04-29 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0020_auto_20180421_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventreservation',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
