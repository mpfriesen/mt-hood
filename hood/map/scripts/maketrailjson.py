import psycopg2
from config import config
import json
from collections import OrderedDict

# query = "SELECT orwa.*,name,state,ST_X(geom),ST_Y(geom) FROM orwa,counties WHERE date=(SELECT MAX(date) FROM orwa) AND orwa.geoid=counties.geoid ORDER BY confirmed DESC;"
# query = "SELECT orwa.*,name,state,pop,ST_X(geom),ST_Y(geom) FROM orwa,counties WHERE orwa.geoid=counties.geoid ORDER BY confirmed DESC;"
# query = "SELECT trail_name,id,ST_AsGeoJSON(geom) from map_trail;"
query = "SELECT jsonb_build_object( \
    'type',     'FeatureCollection', \
    'features', jsonb_agg(features.feature) \
) \
FROM ( \
  SELECT jsonb_build_object( \
    'type',       'Feature', \
    'id',         id, \
    'geometry',   ST_AsGeoJSON(geom)::jsonb, \
    'properties', to_jsonb(inputs) - 'id' - 'geom' \
  ) AS feature \
  FROM (SELECT * FROM map_trail) inputs) features;" \
  
def connect():
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(query)
        json = cur.fetchall()[0][0]
#         for key, value in json.items():
#             print(key)

#         li = []
#         for row in counties:
#             d = OrderedDict()
#             d['type'] = 'Feature'
#             d['id'] = row[1]
#             d['geometry'] = row[2]
#             d['properties'] = {
#                 'name': row[0],
#             }
#             li.append(d)
# 
#         d = OrderedDict()
#         d['type'] = 'FeatureCollection'
#         d['features'] = li
#         print(li)
        
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    with open('/Users/mfriese1/Sites/mt-hood/hood/map/static/map/json/trails.geojson','w') as f:
        f.write(json[0][0].features)       

connect()
  
  
  
  
  
# def connect():
#     conn = None
#     try:
#         params = config()
#         conn = psycopg2.connect(**params)
#         cur = conn.cursor()
#         cur.execute(query)
# 
#         counties = cur.fetchall()
#         li = []
#         for row in counties:
#             d = OrderedDict()
#             d['type'] = 'Feature'
#             d['id'] = row[1]
#             d['geometry'] = row[2]
#             d['properties'] = {
#                 'name': row[0],
#             }
#             li.append(d)
# 
#         d = OrderedDict()
#         d['type'] = 'FeatureCollection'
#         d['features'] = li
# #         print(li)
#         
#         
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if conn is not None:
#             conn.close()
# 
#     with open('/Users/mfriese1/Sites/mt-hood/hood/map/static/map/json/trails.geojson','w') as f:
#         json.dump(d,f,indent=2,default=str)       
# 
# connect()
