# Generated by Django 4.1.7 on 2023-06-02 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0017_remove_device_type_of_device'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='edit_date',
        ),
    ]
