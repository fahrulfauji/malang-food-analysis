"""
Malang Food Analysis - Exploratory Data Analysis

This script performs simple exploratory data analysis (EDA)
on culinary market data from Malang City, Indonesia.

Analysis Included:
1. Top 5 Most Mentioned Menus
2. Top 5 Restaurants by Total Reviews
3. Menu Category Distribution
4. Price Segmentation Distribution
5. Rating Distribution
"""

# ==================================================
# IMPORT LIBRARIES
# ==================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==================================================
# GLOBAL CONFIGURATION
# ==================================================

sns.set_theme(style="whitegrid")

plt.rcParams["figure.dpi"] = 120
plt.rcParams["savefig.dpi"] = 300
plt.rcParams["font.size"] = 11

# ==================================================
# LOAD DATASET
# ==================================================

print("=" * 60)
print("MALANG FOOD ANALYSIS - EXPLORATORY ANALYSIS")
print("=" * 60)

print("\n[1] Loading dataset...")

df = pd.read_csv(
    "data/processed/Malang_City_Food_Dataset_Cleaned.csv"
)

print("✓ Dataset loaded successfully")
print(f"✓ Total menu items : {len(df):,}")
print(f"✓ Total restaurants: {df['Nama_Tempat'].nunique()}")

# ==================================================
# ANALYSIS 1 — TOP 5 MOST MENTIONED MENUS
# ==================================================

print("\n[2] Top 5 Most Mentioned Menus")

top_menu_reviews = (
    df.groupby("Menu")["Jumlah_Ulasan_Menu"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

print(top_menu_reviews)

plt.figure(figsize=(12, 6))

ax = sns.barplot(
    x=top_menu_reviews.values,
    y=top_menu_reviews.index,
    hue=top_menu_reviews.index,
    palette="Blues_r",
    legend=False
)

plt.title(
    "Top 5 Most Mentioned Menus",
    fontsize=16,
    fontweight="bold",
    pad=15
)

plt.xlabel("Total Reviews")
plt.ylabel("")

# Add value labels
for index, value in enumerate(top_menu_reviews.values):
    ax.text(
        value + 10,
        index,
        f"{value:,}",
        va="center",
        fontsize=10
    )

plt.figtext(
    0.125,
    -0.03,
    "Sambal-related menu items appear frequently in customer discussions.",
    fontsize=10,
    style="italic"
)

plt.tight_layout()

plt.savefig(
    "outputs/top5_menus.png",
    bbox_inches="tight"
)

plt.show()

# ==================================================
# ANALYSIS 2 — TOP 5 RESTAURANTS BY TOTAL REVIEWS
# ==================================================

print("\n[3] Top 5 Restaurants by Total Reviews")

top_restaurants = (
    df.groupby("Nama_Tempat")["Jumlah_Total_Ulasan"]
    .max()
    .sort_values(ascending=False)
    .head(5)
)

print(top_restaurants)

plt.figure(figsize=(12, 6))

ax = sns.barplot(
    x=top_restaurants.values,
    y=top_restaurants.index,
    hue=top_restaurants.index,
    palette="crest",
    legend=False
)

plt.title(
    "Top 5 Restaurants by Total Reviews",
    fontsize=16,
    fontweight="bold",
    pad=15
)

plt.xlabel("Total Reviews")
plt.ylabel("")

# Add value labels
for index, value in enumerate(top_restaurants.values):
    ax.text(
        value + 50,
        index,
        f"{value:,}",
        va="center",
        fontsize=10
    )

plt.figtext(
    0.125,
    -0.03,
    "Restaurants with high review counts demonstrate strong online visibility.",
    fontsize=10,
    style="italic"
)

plt.tight_layout()

plt.savefig(
    "outputs/top5_restaurants.png",
    bbox_inches="tight"
)

plt.show()

# ==================================================
# ANALYSIS 3 — MENU CATEGORY DISTRIBUTION
# ==================================================

print("\n[4] Menu Category Distribution")

category_distribution = (
    df["Kategori_Menu"]
    .value_counts()
)

print(category_distribution)

plt.figure(figsize=(10, 6))

ax = sns.barplot(
    x=category_distribution.values,
    y=category_distribution.index,
    hue=category_distribution.index,
    palette="flare",
    legend=False
)

plt.title(
    "Menu Category Distribution",
    fontsize=16,
    fontweight="bold",
    pad=15
)

plt.xlabel("Number of Menu Items")
plt.ylabel("")

# Add value labels
for index, value in enumerate(category_distribution.values):
    ax.text(
        value + 2,
        index,
        f"{value}",
        va="center",
        fontsize=10
    )

plt.figtext(
    0.125,
    -0.03,
    "Complementary and side-dish menus represent a large portion of the dataset.",
    fontsize=10,
    style="italic"
)

plt.tight_layout()

plt.savefig(
    "outputs/category_distribution.png",
    bbox_inches="tight"
)

plt.show()

# ==================================================
# ANALYSIS 4 — PRICE SEGMENTATION DISTRIBUTION
# ==================================================

print("\n[5] Price Segmentation Distribution")

price_distribution = (
    df["Rentang_Harga"]
    .value_counts()
)

print(price_distribution)

plt.figure(figsize=(10, 6))

ax = sns.barplot(
    x=price_distribution.index,
    y=price_distribution.values,
    hue=price_distribution.index,
    palette="mako",
    legend=False
)

plt.title(
    "Price Segmentation Distribution",
    fontsize=16,
    fontweight="bold",
    pad=15
)

plt.xlabel("Price Range")
plt.ylabel("Number of Menu Items")

# Add value labels
for index, value in enumerate(price_distribution.values):
    ax.text(
        index,
        value + 2,
        f"{value}",
        ha="center",
        fontsize=10
    )

plt.figtext(
    0.125,
    -0.03,
    "Affordable and mid-priced menus dominate the dataset.",
    fontsize=10,
    style="italic"
)

plt.tight_layout()

plt.savefig(
    "outputs/price_segmentation.png",
    bbox_inches="tight"
)

plt.show()

# ==================================================
# ANALYSIS 5 — RATING DISTRIBUTION
# ==================================================

print("\n[6] Rating Distribution")

rating_distribution = (
    df["Rating"]
    .value_counts()
    .sort_index()
)

print(rating_distribution)

plt.figure(figsize=(12, 6))

ax = sns.barplot(
    x=rating_distribution.index,
    y=rating_distribution.values,
    hue=rating_distribution.index,
    palette="rocket",
    legend=False
)

plt.title(
    "Restaurant Rating Distribution",
    fontsize=16,
    fontweight="bold",
    pad=15
)

plt.xlabel("Rating")
plt.ylabel("Number of Menu Items")

# Add value labels
for index, value in enumerate(rating_distribution.values):
    ax.text(
        index,
        value + 1,
        f"{value}",
        ha="center",
        fontsize=10
    )

plt.figtext(
    0.125,
    -0.03,
    "Most restaurants maintain ratings above 4.0.",
    fontsize=10,
    style="italic"
)

plt.tight_layout()

plt.savefig(
    "outputs/rating_distribution.png",
    bbox_inches="tight"
)

plt.show()

# ==================================================
# SUMMARY STATISTICS
# ==================================================

print("\n" + "=" * 60)
print("SUMMARY STATISTICS")
print("=" * 60)

print(f"• Total Menu Items       : {len(df):,}")
print(f"• Total Restaurants      : {df['Nama_Tempat'].nunique()}")
print(f"• Average Menu Price     : Rp {df['Harga_Rata_Rata'].mean():,.0f}")
print(f"• Average Rating         : {df['Rating'].mean():.2f}")
print(f"• Total Reviews Analyzed : {df['Jumlah_Ulasan_Menu'].sum():,}")

print("\n" + "=" * 60)
print("✓ Analysis completed successfully")
print("✓ Visualizations exported to outputs/ folder")
print("=" * 60)