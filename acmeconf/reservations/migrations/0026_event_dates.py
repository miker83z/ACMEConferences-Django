# Generated by Django 2.0.3 on 2018-05-02 14:20

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0025_auto_20180502_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='dates',
            field=jsonfield.fields.JSONField(default=[], verbose_name=models.CharField(max_length=200)),
        ),
    ]
