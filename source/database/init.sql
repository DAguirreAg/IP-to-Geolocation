-- Create Database
--CREATE DATABASE db_ip_to_geolocation;

-- Create tables
--- ip_geolocation table
CREATE TABLE db_ip_to_geolocation.public.ip_geolocation_country (
	id SERIAL PRIMARY KEY,
	ip_from BIGINT,
	ip_to BIGINT,
	country_code VARCHAR,
	updated_at timestamptz NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes
--- Index for speeding IP search
CREATE INDEX idx_ip_geolocation_country_ip_from_ip_to ON db_ip_to_geolocation.public.ip_geolocation_country (ip_from, ip_to);