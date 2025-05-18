UPDATE crimes
SET
    type = %(type)s,
    description = %(description)s,
    location = %(location)s,
    suspect_name = %(suspect_name)s,
    date_time = %(date_time)s,
    latitude = %(latitude)s,
    longitude = %(longitude)s
WHERE id = %(crime_id)s
RETURNING
    id, type, description, location, suspect_name, date_time, latitude, longitude;
