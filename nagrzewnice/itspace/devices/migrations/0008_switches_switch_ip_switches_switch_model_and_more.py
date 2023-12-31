# Generated by Django 4.1.7 on 2023-05-30 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0007_remove_switches_switch_port_device_switch_port'),
    ]

    operations = [
        migrations.AddField(
            model_name='switches',
            name='switch_IP',
            field=models.CharField(default='', max_length=16),
        ),
        migrations.AddField(
            model_name='switches',
            name='switch_model',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='switches',
            name='switch_place',
            field=models.CharField(default='', max_length=12),
        ),
        migrations.AlterField(
            model_name='device',
            name='mac_address',
            field=models.CharField(max_length=17),
        ),
        migrations.AlterField(
            model_name='switches',
            name='switch_name',
            field=models.CharField(default='', max_length=9),
        ),
    ]
