CREATE VIEW query1 AS
  SELECT COUNT(*)
  FROM didok_stops
  INNER JOIN osm_stops ON didok_stops.uic_ref = osm_stops.uic_ref;
--> 30829, fast


--- QUERY 2 - List first 100 Didok stations matching stations in OSM.
CREATE VIEW query2 AS
  SELECT did.uic_ref,
         did.name AS didName,
         osm.name as OSMName,
         did.y_koord AS easting,
         did.x_koord AS northing,
         st_astext(st_transform(osm.geom::geometry,21781),0) as geom_wkt, -- 0 decimal places
         st_distance(osm.geom,st_transform(st_setsrid(st_makepoint(y_koord,x_koord),21781),4326)::geometry)::int dist
  FROM didok_stops did
  JOIN osm_stops osm ON did.uic_ref = osm.uic_ref
  ORDER BY did.name
  LIMIT 100;
--> ...


--- QUERY 3 - All Didok stations not identifiable by uic_ref in OSM.
CREATE VIEW query3 AS
  SELECT uic_ref, name, y_koord AS easting, x_koord AS northing
  FROM didok_stops
  WHERE uic_ref NOT IN (
    SELECT d.uic_ref
    FROM didok_stops d
    JOIN osm_stops o ON d.uic_ref = o.uic_ref)
  ORDER BY name;
--> 6278 ...


--- QUERY 4 - Stations in Walenstadt by Bounding Box.
CREATE VIEW query4 AS
  SELECT didok_stops.name, ST_AsText(osm_stops.geom,6) AS geom
  FROM didok_stops
  INNER JOIN osm_stops ON didok_stops.uic_ref = osm_stops.uic_ref
  WHERE ST_Intersects(ST_MakeEnvelope(9.294699,47.110339,9.333789,47.132881, 4326), geom::GEOMETRY)
  ORDER BY 1;
--> 3 rows...


--- QUERY 5 - Stations with name like Walenstadt in Didok.
CREATE VIEW query5 AS
  SELECT didok_stops.name, ST_AsText(osm_stops.geom) AS geom
  FROM didok_stops
  INNER JOIN osm_stops ON didok_stops.uic_ref = osm_stops.uic_ref
  WHERE didok_stops.name LIKE '%walenstadt%'
  ORDER BY 1;
--> 7 rows...


--- QUERY 6 - Stations with matching uic_ref, and name like Walenstadt in either Didok or OSM.
CREATE VIEW query6 AS
  SELECT didok_stops.name AS didok_name,
         osm_stops.name AS osm_name,
         ST_AsText(osm_stops.geom,6) AS geom
  FROM didok_stops
  JOIN osm_stops USING(uic_ref)
  --JOIN osm_stops ON didok_stops.uic_ref = osm_stops.uic_ref
  WHERE (didok_stops.name LIKE '%Walenstadt%'
         OR osm_stops.name LIKE '%Walenstadt%')
  ORDER BY 1;
--> 7 rows ...


--- QUERY 7 - Names that are differ from Didok to OSM.
CREATE VIEW query7 AS
  SELECT didok_stops.name AS didok_name,
         osm_stops.name AS osm_name,
         ST_AsText(osm_stops.geom) AS geom
  FROM didok_stops
  INNER JOIN osm_stops ON didok_stops.uic_ref = osm_stops.uic_ref
  WHERE didok_stops.name != osm_stops.name
  ORDER BY 1;
--> 16138 rows ...


--- QUERY 8a - Stops in Didok but not in OSM (by uic_ref)
CREATE VIEW query8a AS
  SELECT uic_ref,
         "name"
  FROM didok_stops
  WHERE gemeinde != '(Ausland)'
  AND uic_ref NOT IN (SELECT uic_ref FROM osm_stops)
  ORDER BY 1;
--> 5370


--- QUERY 8b - Stops in Didok but not in OSM (by geometry)
CREATE VIEW query8b AS
  SELECT uic_ref,
         "name",
         y_koord AS easting,
         x_koord AS northing
  FROM didok_stops
  WHERE gemeinde = '(Ausland)'
  AND uic_ref NOT IN (SELECT uic_ref FROM osm_stops);


--- QUERY 9 - All stations in canton of St.Gallen in Didok.
CREATE VIEW query9 AS
  SELECT didok_stops.name AS didok_name,
         osm_stops.name AS osm_name,
         ST_AsText(osm_stops.geom) AS geom
  FROM didok_stops
  INNER JOIN osm_stops ON didok_stops.uic_ref = osm_stops.uic_ref
  WHERE didok_stops.kt LIKE 'SG'
  ORDER BY 1;
--> 1631 rows...


--- QUERY 10 - All stations within ...
CREATE VIEW query10 AS
  SELECT count(*) AS cnt
  FROM osm_point
  WHERE (tags->'uic_ref') IS NOT NULL
  AND ST_intersects(geom::geometry, (SELECT geom::geometry FROM osm_polygon WHERE osm_id=-1683941)); -- Stadt St. Gallen
-- 270
/*
SELECT count(*) AS cnt
FROM osm_point
WHERE (tags->'uic_ref') IS NOT NULL
AND ST_intersects(geom::geometry, (SELECT geom::geometry FROM osm_polygon WHERE osm_id=-1687006)) -- SG
--> 1672
*/


--- QUERY 11 - All named OSM objects in canton of St.Gallen.
CREATE VIEW query11 AS
  WITH perimeter AS (
    SELECT geom
    FROM osm_polygon
    WHERE osm_id=-1683941 -- Stadt St. Gallen
  )
  SELECT sum(cnt)
  FROM (
    SELECT count(*) AS cnt
    FROM osm_point, perimeter
    WHERE name IS NOT NULL
    AND st_intersects(osm_point.geom, perimeter.geom)
    UNION ALL
    SELECT count(*)
    FROM osm_line, perimeter
    WHERE name IS NOT NULL
    AND st_intersects(osm_line.geom, perimeter.geom)
    UNION ALL
    SELECT count(*)
    FROM osm_polygon, perimeter
    WHERE name IS NOT NULL
    AND st_intersects(osm_polygon.geom, perimeter.geom)
  )
  all_counts;
--> 4620


--- QUERY 12 - Benannte Objekte rund 47.22679/8.81652 im Umkreis 15m.
CREATE VIEW query12 AS
  SELECT
    osm_id,
    name,
    ST_AsText(geom) AS geom
  FROM osm_point
  WHERE name is not null
  AND ST_DWithin(ST_GeomFromText('POINT(8.81652 47.22679)',4326), geom, 15)
  ORDER BY name;
--> 4280011859|"Jakob"|"POINT(8.81651 47.22679)"
--> 1355269682|"Jakob Hotel am Hauptplatz"|"POINT(8.8165 47.22685)"


-- QUERY 13 - Restaurants 300 Meter ums Zentrum von Rapperswil-Jona
CREATE VIEW query13 AS
  SELECT
    osm_id,
    name,
    ST_AsText(osm_point.geom,6) AS geom
  FROM osm_point
  WHERE (tags @> 'amenity=>restaurant'::hstore)
  AND st_intersects(geom, st_buffer(ST_GeogFromText('POINT(8.816841 47.224955)'), 300))
  ORDER BY name;
  --> 23 rows


--- QUERY 14 - Restaurants im Umkreis 15m vom Bahnhof Rapperswil.
CREATE VIEW query14 AS
  SELECT
    osm_id,
    name,
    st_distance(osm.geom, perimeter.geom)::int AS dist
  FROM
    osm_point AS osm,
    (SELECT ST_GeomFromText('POINT(8.81652 47.22679)',4326)::geography AS geom) AS perimeter
  WHERE (osm.tags->'amenity') IS NOT null
  AND ST_DWithin(osm.geom, perimeter.geom, 100)
  ORDER BY st_distance(osm.geom, perimeter.geom) DESC;
--> 22 rows.

CREATE VIEW didok_osm AS
  SELECT didok_stops.uic_ref as didok_uic_ref,ld, dst_nr, kz, didok_stops.name as didok_name, laenge, namel, dst_abk, go_nr, go_abk, gde_nr,gemeinde, kt, bp, vp, vg, vd,y_koord, x_koord, hoehe, osm_stops.uic_ref as osm_stops_uic_ref, geom, didok_stops.name as osm_stops_name, osm_id
  FROM didok_stops
  INNER JOIN osm_stops ON didok_stops.uic_ref = osm_stops.uic_ref;
