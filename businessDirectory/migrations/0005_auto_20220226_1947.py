# Generated by Django 3.1.5 on 2022-02-26 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('businessDirectory', '0004_auto_20220226_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='logo',
            field=models.ImageField(default='static/uploads/logos/no-image.png', upload_to='static/uploads/logos/'),
        ),
    ]
