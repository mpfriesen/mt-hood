from django.contrib.gis import admin
from .models import SnoPark, Trail, RecPoint, Death, TrailType, Activity, ActivJoin, TrailJoin, Photo


admin.site.register(SnoPark, admin.GeoModelAdmin)
admin.site.register(Trail, admin.GeoModelAdmin)
admin.site.register(RecPoint, admin.GeoModelAdmin)
admin.site.register(Death, admin.GeoModelAdmin)
admin.site.register(TrailType, admin.GeoModelAdmin)
admin.site.register(Activity, admin.GeoModelAdmin)
admin.site.register(Photo, admin.GeoModelAdmin)