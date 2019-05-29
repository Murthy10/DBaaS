create extension pg_prewarm;

SELECT pg_prewarm('actor');
SELECT pg_prewarm('address');
SELECT pg_prewarm('category');
SELECT pg_prewarm('city');
SELECT pg_prewarm('country');
SELECT pg_prewarm('customer');
SELECT pg_prewarm('film');
SELECT pg_prewarm('film_actor');
SELECT pg_prewarm('film_category');
SELECT pg_prewarm('inventory');
SELECT pg_prewarm('language');
SELECT pg_prewarm('payment');
SELECT pg_prewarm('rental');
SELECT pg_prewarm('staff');
SELECT pg_prewarm('store');
