# Generated by Django 3.1.5 on 2022-02-27 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('businessDirectory', '0008_auto_20220227_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='customermessage',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='notification',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
    ]
