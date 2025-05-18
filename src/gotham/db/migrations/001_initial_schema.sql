-- Create crimes table
CREATE TABLE IF NOT EXISTS crimes (
    id SERIAL PRIMARY KEY,
    type VARCHAR(50) NOT NULL,
    description VARCHAR(255) NOT NULL,
    location VARCHAR(255) NOT NULL,
    suspect_name VARCHAR(50) NOT NULL,
    date_time TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL
);

-- Insert some sample data
INSERT INTO crimes (type, description, location, suspect_name, date_time, latitude, longitude) VALUES
    ('murder', 'John Doe was found dead in his home', '123 Main St, Gotham, USA', 'Joker', '2025-05-17 18:10:00', 37.7749, -122.4194),
    ('robbery', 'Suspect robbed a convenience store', '456 Oak Ave, Gotham, USA', 'Pinguin', '2025-05-16 10:10:00', 37.7412, -122.4729),
    ('arson', 'Gotham City Hall set ablaze during mayoral speech', '100 Gotham City Hall, Gotham, USA', 'Firefly', '2025-05-15 21:30:00', 37.7793, -122.4192),
    ('kidnapping', 'Commissioner Gordon''s daughter abducted from her apartment', '789 Park Row, Gotham, USA', 'Two-Face', '2025-05-14 23:45:00', 37.7800, -122.4200),
    ('theft', 'Priceless diamond stolen from Gotham Museum', '1 Museum Dr, Gotham, USA', 'Catwoman', '2025-05-13 02:15:00', 37.7812, -122.4175),
    ('assault', 'Security guards attacked at Wayne Enterprises', '500 Wayne Tower, Gotham, USA', 'Bane', '2025-05-12 18:00:00', 37.7890, -122.4100),
    ('poisoning', 'City reservoir contaminated, mass panic ensues', 'Gotham Reservoir, Gotham, USA', 'Poison Ivy', '2025-05-11 07:30:00', 37.7700, -122.4300),
    ('bank robbery', 'Gotham National Bank vault emptied overnight', '200 Bank St, Gotham, USA', 'Riddler', '2025-05-10 03:00:00', 37.7755, -122.4180)
ON CONFLICT (id) DO NOTHING;