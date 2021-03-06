# Generated by Django 3.1.7 on 2021-04-11 17:25

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('map', '0001_initial'), ('map', '0002_auto_20210407_0700'), ('map', '0003_trail'), ('map', '0004_auto_20210408_0741'), ('map', '0005_auto_20210408_0745'), ('map', '0006_auto_20210411_0306'), ('map', '0007_auto_20210411_0333'), ('map', '0008_auto_20210411_0338'), ('map', '0009_auto_20210411_0352'), ('map', '0010_auto_20210411_0356'), ('map', '0011_auto_20210411_0357'), ('map', '0012_auto_20210411_0400'), ('map', '0013_auto_20210411_0402'), ('map', '0014_auto_20210411_0729'), ('map', '0015_auto_20210411_1721')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SnoPark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('desc', models.CharField(max_length=254)),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('activity', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RecPoint',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=254, null=True)),
                ('area', models.CharField(max_length=254)),
                ('actlist', models.CharField(max_length=254)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='TrailJoin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='trail',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('trail_no', models.CharField(max_length=254, null=True)),
                ('trail_name', models.CharField(max_length=254, null=True)),
                ('length_mil', models.FloatField(null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiLineStringField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='TrailType',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('ttype', models.CharField(max_length=100)),
                ('trails', models.ManyToManyField(through='map.TrailJoin', to='map.Trail')),
            ],
        ),
        migrations.AddField(
            model_name='trailjoin',
            name='trail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='map.trail'),
        ),
        migrations.AddField(
            model_name='trailjoin',
            name='trailtype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='map.trailtype'),
        ),
        migrations.CreateModel(
            name='ActivJoin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='map.activity')),
                ('recpoint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='map.recpoint')),
            ],
        ),
        migrations.AddField(
            model_name='activity',
            name='points',
            field=models.ManyToManyField(through='map.ActivJoin', to='map.RecPoint'),
        ),
        migrations.AlterField(
            model_name='trailtype',
            name='trails',
            field=models.ManyToManyField(through='map.TrailJoin', to='map.Trail'),
        ),
        migrations.AlterField(
            model_name='trailtype',
            name='trails',
            field=models.ManyToManyField(through='map.TrailJoin', to='map.Trail'),
        ),
        migrations.AlterField(
            model_name='trailtype',
            name='trails',
            field=models.ManyToManyField(through='map.TrailJoin', to='map.Trail'),
        ),
        migrations.AlterField(
            model_name='trailtype',
            name='trails',
            field=models.ManyToManyField(through='map.TrailJoin', to='map.Trail'),
        ),
        migrations.AlterField(
            model_name='trailtype',
            name='trails',
            field=models.ManyToManyField(through='map.TrailJoin', to='map.Trail'),
        ),
        migrations.CreateModel(
            name='Death',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, null=True)),
                ('age', models.CharField(max_length=10, null=True)),
                ('city', models.CharField(max_length=254, null=True)),
                ('state', models.CharField(max_length=254, null=True)),
                ('location', models.CharField(max_length=254, null=True)),
                ('month', models.CharField(max_length=254, null=True)),
                ('year', models.IntegerField()),
                ('activity', models.CharField(max_length=254, null=True)),
                ('cause_death', models.CharField(max_length=254, null=True)),
                ('desc', models.CharField(max_length=254, null=True)),
                ('link', models.CharField(max_length=254, null=True)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
        migrations.AlterField(
            model_name='trailtype',
            name='trails',
            field=models.ManyToManyField(through='map.TrailJoin', to='map.Trail'),
        ),
        migrations.AlterField(
            model_name='trailtype',
            name='trails',
            field=models.ManyToManyField(through='map.TrailJoin', to='map.Trail'),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('desc', models.TextField()),
                ('cover', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.AlterField(
            model_name='trailtype',
            name='trails',
            field=models.ManyToManyField(through='map.TrailJoin', to='map.Trail'),
        ),
        migrations.AlterField(
            model_name='trailtype',
            name='trails',
            field=models.ManyToManyField(through='map.TrailJoin', to='map.Trail'),
        ),
    ]
