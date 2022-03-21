# Generated by Django 3.1.5 on 2022-03-02 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('businessDirectory', '0012_auto_20220228_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='address',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='business',
            name='email',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='business',
            name='landmark',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='business',
            name='latitude',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='business',
            name='longitude',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='business',
            name='phone',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
