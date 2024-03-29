# Generated by Django 4.1.6 on 2023-02-26 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0012_alter_landing_type_block'),
    ]

    operations = [
        migrations.AddField(
            model_name='landing',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='landing',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Видимость'),
        ),
    ]
