-- =========================================================
-- MALANG FOOD ANALYSIS - EXPLORATORY SQL QUERIES
-- =========================================================

-- Project:
-- Exploratory analysis of restaurant and menu trends
-- in Malang City using MySQL.

USE malang_food_analysis;

-- =========================================================
-- QUERY 1 — TOTAL DATA OVERVIEW
-- =========================================================
-- Objective:
-- Measure dataset size and restaurant coverage.

SELECT
    COUNT(*) AS total_menu_items,
    COUNT(DISTINCT Nama_Tempat) AS total_restaurants
FROM restaurants;

-- =========================================================
-- QUERY 2 — MENU CATEGORY DISTRIBUTION
-- =========================================================
-- Objective:
-- Identify menu category distribution.

SELECT
    Kategori_Menu AS menu_category,
    COUNT(*) AS total_menu_items,
    ROUND(
        COUNT(*) * 100.0 /
        (SELECT COUNT(*) FROM restaurants),
        1
    ) AS percentage_distribution
FROM restaurants
GROUP BY Kategori_Menu
ORDER BY total_menu_items DESC;

-- =========================================================
-- QUERY 3 — AVERAGE PRICE BY MENU CATEGORY
-- =========================================================
-- Objective:
-- Compare average menu pricing across categories.

SELECT
    Kategori_Menu AS menu_category,
    ROUND(AVG(Harga_Rata_Rata), 0) AS average_price
FROM restaurants
GROUP BY Kategori_Menu
ORDER BY average_price DESC;

-- =========================================================
-- QUERY 4 — TOP 5 RESTAURANTS BY TOTAL REVIEWS
-- =========================================================
-- Objective:
-- Identify restaurants with the highest review volume.

SELECT
    Nama_Tempat AS restaurant_name,
    MAX(Jumlah_Total_Ulasan) AS total_reviews,
    ROUND(AVG(Rating), 2) AS average_rating
FROM restaurants
GROUP BY Nama_Tempat
ORDER BY total_reviews DESC
LIMIT 5;

-- =========================================================
-- QUERY 5 — RATING DISTRIBUTION
-- =========================================================
-- Objective:
-- Analyze restaurant rating distribution.

SELECT
    ROUND(Rating, 1) AS rating_score,
    COUNT(*) AS total_records
FROM restaurants
GROUP BY ROUND(Rating, 1)
ORDER BY rating_score DESC;

-- =========================================================
-- QUERY 6 — MOST REVIEWED MENU ITEMS
-- =========================================================
-- Objective:
-- Identify menu items with the highest review volume.

SELECT
    Menu AS menu_item,
    SUM(Jumlah_Ulasan_Menu) AS total_menu_reviews
FROM restaurants
GROUP BY Menu
ORDER BY total_menu_reviews DESC
LIMIT 10;

-- =========================================================
-- QUERY 7 — PRICE SEGMENT DISTRIBUTION
-- =========================================================
-- Objective:
-- Analyze menu price segment distribution.

-- Additional cleaning:
-- TRIM() and REPLACE() are used to remove
-- hidden line-break characters from imported CSV data.

SELECT
    TRIM(REPLACE(Rentang_Harga, '\r', '')) AS price_range,
    COUNT(*) AS total_menu_items,
    ROUND(AVG(Rating), 2) AS average_rating
FROM restaurants
GROUP BY TRIM(REPLACE(Rentang_Harga, '\r', ''))
ORDER BY total_menu_items DESC;