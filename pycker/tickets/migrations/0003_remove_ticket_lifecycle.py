# Generated by Django 3.2.6 on 2021-08-04 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='lifecycle',
        ),
    ]