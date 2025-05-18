DELETE FROM crimes
WHERE id = %(crime_id)s
RETURNING id;
