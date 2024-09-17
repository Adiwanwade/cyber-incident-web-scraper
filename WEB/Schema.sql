-- Table Creation 

CREATE DATABASE IF NOT EXISTS CyberPulse_DB;
USE CyberPulse_DB;

CREATE TABLE IF NOT EXISTS Incidents (
    incident_title VARCHAR(50) NOT NULL,
    incident_date DATE NOT NULL,
    incident_description TEXT NOT NULL,
    incident_website VARCHAR(50) NOT NULL,
    incident_location VARCHAR(50) NOT NULL,
    incident_reporter VARCHAR(20) NOT NULL,
    incident_comments TEXT,
);

CREATE TABLE IF NOT EXISTS Users (
    username VARCHAR(20) UNIQUE NOT NULL,
    password TEXT NOT NULL,
    recommends 
);