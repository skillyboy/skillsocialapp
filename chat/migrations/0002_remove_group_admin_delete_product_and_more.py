# Generated by Django 4.0.5 on 2022-08-24 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='admin',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='processor',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='user',
        ),
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.DeleteModel(
            name='Processor',
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
    ]
