# Generated by Django 2.0.3 on 2018-05-02 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0027_auto_20180502_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='contDeadline',
            field=models.DateTimeField(auto_now=True, verbose_name='contribution deadline'),
        ),
        migrations.AlterField(
            model_name='event',
            name='subsDeadline',
            field=models.DateTimeField(auto_now=True, verbose_name='subscriptions deadline'),
        ),
        migrations.AlterField(
            model_name='event',
            name='subsStart',
            field=models.DateTimeField(auto_now=True, verbose_name='subscriptions start'),
        ),
    ]