# Generated by Django 4.0.1 on 2023-02-15 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0005_alter_brick_friends_alter_landing_friends'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='landing',
            name='cat',
        ),
        migrations.RemoveField(
            model_name='landing',
            name='friends',
        ),
    ]