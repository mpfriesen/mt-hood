import psycopg2
from config import config
import json
from collections import OrderedDict

# query = "SELECT orwa.*,name,state,ST_X(geom),ST_Y(geom) FROM orwa,counties WHERE date=(SELECT MAX(date) FROM orwa) AND orwa.geoid=counties.geoid ORDER BY confirmed DESC;"
# query = "SELECT orwa.*,name,state,pop,ST_X(geom),ST_Y(geom) FROM orwa,counties WHERE orwa.geoid=counties.geoid ORDER BY confirmed DESC;"
query = "SELECT name,age,city,state,location,month,year,activity,map_death.desc,link,id,ST_X(geom),ST_Y(geom) from map_death;"

def connect():
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(query)

        counties = cur.fetchall()
        li = []
        for row in counties:
            d = OrderedDict()
            d['type'] = 'Feature'
            d['id'] = row[10]
            d['geometry'] = {
                'type': 'Point',
                'coordinates': [row[11], row[12]]
            }
            d['properties'] = {
                'name': row[0],
                'age': row[1],
                'city': row[2],
                'state': row[3],
                'location': row[4],
                'month': row[5],
                'year': row[6],
                'activity': row[7],
                'description': row[8],
                'link': row[9],
                'id': row[10]
            }
            li.append(d)

        d = OrderedDict()
        d['type'] = 'FeatureCollection'
        d['features'] = li
#         print(li)
        
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    with open('/Users/mfriese1/Sites/mt-hood/hood/map/static/map/json/deaths.geojson','w') as f:
        json.dump(d,f,indent=2,default=str)       

connect()
