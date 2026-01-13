-- ============================================
-- MALANG FOOD ANALYSIS - SIMPLE SQL QUERIES
-- ============================================

-- Make sure you use the correct database
USE malang_food_analysis;

-- ============================================
-- QUERY 1: Total data count
-- ============================================
SELECT 
    COUNT(*) AS total_menu 
FROM restaurants;


-- ============================================
-- QUERY 2: Category Distribution
-- ============================================
SELECT 
    Kategori_Menu,
    COUNT(*) AS jumlah_menu
FROM restaurants
GROUP BY Kategori_Menu;


-- ============================================
-- QUERY 3: Average price
-- ============================================
SELECT 
    Kategori_Menu,
    AVG(Harga_Rata_Rata) AS harga_rata_rata
FROM restaurants
GROUP BY Kategori_Menu;


-- ============================================
-- QUERY 4: Top 5 Restaurants By Reviews
-- ============================================
SELECT 
    Nama_Tempat,
    MAX(Jumlah_Total_Ulasan) AS total_ulasan
FROM restaurants
GROUP BY Nama_Tempat
ORDER BY total_ulasan DESC
LIMIT 5;


-- ============================================
-- QUERY 5: Rating Distribution
-- ============================================
SELECT 
    ROUND(Rating, 1) AS rating,
    COUNT(*) AS jumlah_menu
FROM restaurants
GROUP BY ROUND(Rating, 1)
ORDER BY rating DESC;