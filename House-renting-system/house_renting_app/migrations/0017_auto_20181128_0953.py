# Generated by Django 2.1.2 on 2018-11-28 09:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house_renting_app', '0016_auto_20181128_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='apartment_owner_number',
            field=models.PositiveIntegerField(default=0, null=True, validators=[django.core.validators.MaxValueValidator(9999999999)]),
        ),
    ]
