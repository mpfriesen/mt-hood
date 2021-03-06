# Generated by Django 3.1.7 on 2021-04-12 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0005_auto_20210411_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='death',
            name='activity',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='death',
            name='age',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='death',
            name='cause_death',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='death',
            name='city',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='death',
            name='desc',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='death',
            name='link',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='death',
            name='location',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='death',
            name='name',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='death',
            name='state',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='recpoint',
            name='name',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='trail',
            name='length_mil',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trail',
            name='trail_name',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='trail',
            name='trail_no',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='trailtype',
            name='trails',
            field=models.ManyToManyField(through='map.TrailJoin', to='map.Trail'),
        ),
    ]
