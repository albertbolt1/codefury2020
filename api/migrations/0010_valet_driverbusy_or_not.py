# Generated by Django 3.1.3 on 2020-11-07 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20201108_0211'),
    ]

    operations = [
        migrations.AddField(
            model_name='valet',
            name='driverbusy_or_not',
            field=models.BooleanField(default=False),
        ),
    ]
