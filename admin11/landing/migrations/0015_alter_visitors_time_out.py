# Generated by Django 4.1.6 on 2023-05-10 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0014_visitors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitors',
            name='time_out',
            field=models.CharField(blank=True, db_index=True, max_length=100, verbose_name='Визитов'),
        ),
    ]
