"SELECT jsonb_build_object( \
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
  FROM (SELECT * FROM map_trail) inputs) features;"