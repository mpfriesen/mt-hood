# Generated by Django 3.1.7 on 2021-04-11 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0004_auto_20210411_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trailtype',
            name='trails',
            field=models.ManyToManyField(through='map.TrailJoin', to='map.Trail'),
        ),
    ]
