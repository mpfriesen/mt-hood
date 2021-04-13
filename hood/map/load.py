from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import SnoPark, Trail, Death, RecPoint

snopark_mapping = {
    'name': 'name',
    'desc': 'desc',
    'point': 'POINT',
}


trail_mapping = {
    'trail_no': 'TRAIL_NO',
    'trail_name': 'Trail_Name',
    'length_mil': 'Length_Mil',
    'id': 'id',
    'geom': 'MULTILINESTRING',
}



death_mapping = {
    'name': 'Name',
    'age': 'Age',
    'city': 'City',
    'state': 'State',
    'location': 'Location',
    'month': 'Month',
    'year': 'Year',
    'activity': 'Activity',
    'cause_death': 'Cause_Deat',
    'desc': 'Circumstan',
    'link': 'Link',
    'lat': 'lat',
    'lng': 'lng',
    'geom': 'POINT',
}


recpoint_mapping = {
    'name': 'name',
    'area': 'area',
    'id': 'id',
    'actlist': 'actlist',
    'geom': 'POINT',
}

trail_shp = Path(__file__).resolve().parent / 'data' / 'hoodtrail.shp'
snopark_shp = Path(__file__).resolve().parent / 'data' / 'sno-parks.shp'
recpoint_shp = Path(__file__).resolve().parent / 'data' / 'recpoint.shp'
death_shp = Path(__file__).resolve().parent / 'data' / 'death.shp'

def run(verbose=True):
    lm = LayerMapping(SnoPark, str(snopark_shp), snopark_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)


