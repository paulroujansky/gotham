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
    ('robbery', 'Suspect robbed a convenience store', '456 Oak Ave, Gotham, USA', 'Pinguin', '2025-05-16 10:10:00', 37.7412, -122.4729)
ON CONFLICT (id) DO NOTHING; 