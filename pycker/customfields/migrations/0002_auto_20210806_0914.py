# Generated by Django 3.2.6 on 2021-08-06 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customfields', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customfield',
            name='multiple',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='objcustomfieldvalues',
            name='value',
            field=models.TextField(default='', null=True),
        ),
    ]