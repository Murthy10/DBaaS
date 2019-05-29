create extension pg_prewarm;

SELECT pg_prewarm('didok_stops');
SELECT pg_prewarm('osm_line');
SELECT pg_prewarm('osm_point');
SELECT pg_prewarm('osm_polygon');
SELECT pg_prewarm('osm_stops');
SELECT pg_prewarm('spatial_ref_sys');

