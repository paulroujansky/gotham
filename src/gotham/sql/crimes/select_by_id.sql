SELECT
    id,
    type,
    description,
    location,
    suspect_name,
    date_time,
    latitude,
    longitude
FROM crimes
WHERE id = %(crime_id)s;
