# Generated by Django 2.0.7 on 2018-07-19 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_remove_device_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='pin',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='raspberry.GPIO_pins'),
        ),
    ]
