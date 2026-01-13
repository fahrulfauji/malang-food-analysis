-- =========================================
-- SIMPLE DATABASE SETUP
-- Malang Food Analysis - Basic Schema
-- =========================================

-- 1. CREATE DATABASE (if not exists)
CREATE DATABASE IF NOT EXISTS malang_food_analysis;
USE malang_food_analysis;

-- 2. DROP TABLE IF EXISTS (for clean setup)
DROP TABLE IF EXISTS restaurants;

-- 3. CREATE TABLE STATEMENT
CREATE TABLE restaurants (
    `No` INT,
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

-- 4. SIMPLE COMMENT
-- This table contains 372 menu items from 89 restaurants in Malang
-- Data source: Google Maps (manual collection, Sep 2025)