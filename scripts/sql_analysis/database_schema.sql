-- =========================================
-- MALANG FOOD ANALYSIS - DATABASE SCHEMA
-- =========================================
DROP database malang_food_analysis;

-- Create database
CREATE DATABASE IF NOT EXISTS malang_food_analysis;

-- Select database
USE malang_food_analysis;

-- Remove old table before re-import
DROP TABLE IF EXISTS restaurants;

-- =========================================
-- CREATE TABLE: restaurants
-- =========================================

CREATE TABLE restaurants (
    `No` INT PRIMARY KEY,
    `Nama_Tempat` VARCHAR(255),
    `Kecamatan` VARCHAR(100),
    `Menu` VARCHAR(255),
    `Jumlah_Ulasan_Menu` INT,
    `Jumlah_Total_Ulasan` INT,
    `Rating` DECIMAL(3,1),
    `Harga_Minimal` INT,
    `Harga_Maksimal` INT,
    `Harga_Min_Clean` INT,
    `Harga_Max_Clean` INT,
    `Kategori_Menu` VARCHAR(50),
    `Harga_Rata_Rata` INT,
    `Rentang_Harga` VARCHAR(50)
);

-- =========================================
-- TABLE INFORMATION
-- =========================================
-- This table contains:
-- • 372 menu items
-- • 89 restaurants
-- • Culinary data collected manually from Google Maps
-- • Location: Malang City, Indonesia
-- • Collection period: January 2026

-- =========================================
-- LOAD CSV DATA
-- =========================================

LOAD DATA INFILE 'C:/ProgramData/MySQL/MYSQL Server 8.0/Uploads/Malang_City_Food_Dataset_Cleaned.csv'
INTO TABLE restaurants
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

-- =========================================
-- VALIDATION QUERIES
-- =========================================

-- Check imported rows
SELECT COUNT(*) AS total_rows
FROM restaurants;

-- Preview dataset
SELECT *
FROM restaurants
LIMIT 5;