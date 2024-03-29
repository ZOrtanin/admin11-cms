# Generated by Django 4.0.1 on 2023-02-15 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0003_landing_friends_alter_landing_cat_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brick',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('friends', models.ManyToManyField(to='landing.Brick')),
            ],
        ),
        migrations.AlterField(
            model_name='landing',
            name='friends',
            field=models.ManyToManyField(to='landing.Brick'),
        ),
    ]
