# Generated by Django 5.0 on 2023-12-31 07:48

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_dealership_admin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='admincardealershipmodel',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=254),
            preserve_default=False,
        ),
    ]