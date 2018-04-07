# Generated by Django 2.0.3 on 2018-04-06 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0005_event_ticket_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='seats',
            new_name='available_seats',
        ),
        migrations.AddField(
            model_name='event',
            name='max_seats',
            field=models.IntegerField(default=0),
        ),
    ]
