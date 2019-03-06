# Generated by Django 2.1.2 on 2018-11-16 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house_renting_app', '0004_hostels_houses'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='images1',
            field=models.ImageField(null=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='images2',
            field=models.ImageField(null=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='images3',
            field=models.ImageField(null=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='hostels',
            name='images4',
            field=models.ImageField(null=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='hostels',
            name='images5',
            field=models.ImageField(null=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='hostels',
            name='images6',
            field=models.ImageField(null=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='houses',
            name='images7',
            field=models.ImageField(null=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='houses',
            name='images9',
            field=models.ImageField(null=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='houses',
            name='imgages8',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
