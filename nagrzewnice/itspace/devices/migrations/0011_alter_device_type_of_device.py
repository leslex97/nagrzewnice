# Generated by Django 4.1.7 on 2023-06-02 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0010_alter_device_type_of_device'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='type_of_device',
            field=models.CharField(choices=[('AP', 'Access Point'), ('D', 'Desktop'), ('N', 'Notebook'), ('E', 'Etykieciarka'), ('Z', 'Zebra'), ('TV', 'Telewizor'), ('P', 'Printer')], max_length=30),
        ),
    ]
