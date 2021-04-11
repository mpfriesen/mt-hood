# Generated by Django 3.1.7 on 2021-04-11 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0011_auto_20210411_0357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='death',
            name='age',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='trailtype',
            name='trails',
            field=models.ManyToManyField(through='map.TrailJoin', to='map.Trail'),
        ),
    ]