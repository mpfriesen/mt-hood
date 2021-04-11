from django.contrib.gis.db import models

# Create your models here.

class SnoPark(models.Model):
    name = models.CharField(max_length=254)
    desc = models.CharField(max_length=254)
    point = models.PointField()
    
    def __str__(self):
        return self.name
        
    
class Trail(models.Model):
    id = models.BigIntegerField(primary_key=True)
    trail_no = models.CharField(max_length=254, null=True)
    trail_name = models.CharField(max_length=254, null=True)
    length_mil = models.FloatField(null=True)
    geom = models.MultiLineStringField(srid=4326)

    def __str__(self):
        return self.trail_name or ''


class TrailType(models.Model):
    id = models.BigIntegerField(primary_key=True)
    ttype = models.CharField(max_length=100)
    trails = models.ManyToManyField(Trail,through='TrailJoin')
    
    def __str__(self):
        return self.ttype
    


class TrailJoin(models.Model):
    trail = models.ForeignKey(Trail, on_delete=models.CASCADE)
    trailtype = models.ForeignKey(TrailType, on_delete=models.CASCADE)



class Death(models.Model):
    name = models.CharField(max_length=254, null=True)
    age = models.CharField(max_length=10, null=True)
    city = models.CharField(max_length=254, null=True)
    state = models.CharField(max_length=254, null=True)
    location = models.CharField(max_length=254, null=True)
    month = models.CharField(max_length=254, null=True)
    year = models.IntegerField()
    activity = models.CharField(max_length=254, null=True)
    cause_death = models.CharField(max_length=254, null=True)
    desc = models.CharField(max_length=254, null=True)
    link = models.CharField(max_length=254, null=True)
    lat = models.FloatField()
    lng = models.FloatField()
    geom = models.PointField(srid=4326)

    def __str__(self):
        return self.name or ''


class RecPoint(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=254, null=True)
    area = models.CharField(max_length=254)
    actlist = models.CharField(max_length=254)
    geom = models.PointField(srid=4326)

    def __str__(self):
        return self.name or ''
        
class Activity(models.Model):
    id = models.BigIntegerField(primary_key=True)
    activity = models.CharField(max_length=100)
    points = models.ManyToManyField(RecPoint, through='ActivJoin')
    
    def __str__(self):
        return self.activity
        
class ActivJoin(models.Model):
    recpoint = models.ForeignKey(RecPoint, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    
    
class Photo(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

