INSERT INTO crimes (
    type, description, location, suspect_name, date_time, latitude, longitude
)
VALUES (
    %(type)s, %(description)s, %(location)s, %(suspect_name)s, %(date_time)s, %(latitude)s, %(longitude)s
)
RETURNING
    id, type, description, location, suspect_name, date_time, latitude, longitude;
