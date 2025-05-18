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
ORDER BY date_time DESC
LIMIT %(limit)s OFFSET %(skip)s;
