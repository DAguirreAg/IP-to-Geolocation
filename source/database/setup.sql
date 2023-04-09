-- Create Feedback Database
CREATE DATABASE db_ip_to_geolocation;

-- Create tables
--- ip_geolocation table
CREATE TABLE ip_geolocation (
	id SERIAL PRIMARY KEY,
	ip_from BIGINT,
	ip_to BIGINT,
	country VARCHAR,
	updated_at timestamptz NOT NULL DEFAULT CURRENT_TIMESTAMP
);