"""
Malang Trend Food Analysis - Simple Analysis Script
This script performs a simple analysis of the Malang City Food Dataset and generates 5 key insights with visualizations.
The insights include:   
1. Top 5 Menu with the Most Reviews
2. Top 5 Restaurants by Reviews
3. Menu Category Distribution
4. Price Segmentation
5. Rating Distribution
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("=" * 50)
print("MALANG FOOD - 5 SIMPLE INSIGHTS")
print("=" * 50)

# Set seaborn style for better looking charts
sns.set_style("whitegrid")
sns.set_palette("husl")

# 1. LOAD DATA
print("\n[1] Loading data...")
df = pd.read_csv('data/Malang_City_Food_Dataset_Cleaned.csv')
print(f"✓ Loaded: {len(df)} rows, {df['Nama_Tempat'].nunique()} restaurants")

# ============================================
# INSIGHT 1: TOP 5 MENU WITH THE MOST REVIEWS 
# ============================================
print("\n[2] Insight 1: Top 5 Most Mentioned Menus")

menu_reviews = df.groupby('Menu')['Jumlah_Ulasan_Menu'].sum()
top5_menu = menu_reviews.sort_values(ascending=False).head(5)

print("Top 5 Menus")
for i, (menu, reviews) in enumerate(top5_menu.items(), 1):
    print(f"  {i}. {menu}: {reviews:,} views")

plt.figure(figsize=(10, 5))
sns.barplot(x=top5_menu.values, y=top5_menu.index, palette="Blues_d")
plt.title('Top 5 Most Mentioned Menus', fontsize=14, fontweight='bold')
plt.xlabel('Number of Reviews')
plt.ylabel('')

# Add value labels
for i, v in enumerate(top5_menu.values):
    plt.text(v + 5, i, f'{v:,}', va='center', fontsize=10)

plt.tight_layout()
plt.savefig('outputs/top5_menus.png', dpi=300, bbox_inches='tight')
plt.show()

# ============================================
# INSIGHT 2: TOP 5 RESTAURANTS BY REVIEWS
# ============================================
print("\n[3] Insight 2: Top 5 Most Popular Restaurants")

resto_reviews = df.groupby('Nama_Tempat')['Jumlah_Total_Ulasan'].max()
top5_resto = resto_reviews.sort_values(ascending=False).head(5)

print("Top 5 Restaurants")
for i, (resto, reviews) in enumerate(top5_resto.items(), 1):
    print(f"  {i}. {resto}: {reviews:,} reviews")

plt.figure(figsize=(10, 5))
sns.barplot(x=top5_resto.values, y=top5_resto.index, palette="Greens_d")
plt.title('TOP 5 MOST POPULAR RESTAURANTS', fontsize=14, fontweight='bold')
plt.xlabel('Number of Reviews')
plt.ylabel('')

for i, v in enumerate(top5_resto.values):
    plt.text(v + 50, i, f'{v:,}', va='center', fontsize=10)

plt.tight_layout()
plt.savefig('outputs/top5_restaurants.png', dpi=300, bbox_inches='tight')
plt.show()

# ============================================
# INSIGHT 3: MENU CATEGORY DISTRIBUTION
# ============================================
print("\n[4] Insight 3: Menu Category Distribution")

category_counts = df['Kategori_Menu'].value_counts()
print("Category Distribution:")
for i, (category, count) in enumerate(category_counts.items(), 1):
    percentage = (count / len(df)) * 100
    print(f"  {i}. {category}: {count} menu ({percentage:.1f}%)")

plt.figure(figsize=(8, 8))
colors = sns.color_palette("pastel")[0:3]
plt.pie(category_counts.values, labels=category_counts.index, autopct='%1.1f%%', 
        colors=colors, startangle=90)
plt.title('MENU CATEGORY DISTRIBUTION', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('outputs/category_distribution.png', dpi=300, bbox_inches='tight')
plt.show()

# ============================================
# INSIGHT 4: PRICE SEGMENTATION 
# ============================================
print("\n[5] Insight 4: Price Segmentation")

price_counts = df['Rentang_Harga'].value_counts()
print("Price Segmentation:")
for i, (price_range, count) in enumerate(price_counts.items(), 1):
    percentage = (count / len(df)) * 100
    print(f"  {i}. {price_range}: {count} menu ({percentage:.1f}%)")

plt.figure(figsize=(8, 8))
colors = sns.color_palette("Set2")[0:3]
plt.pie(price_counts.values, labels=price_counts.index, autopct='%1.1f%%', 
        colors=colors, startangle=90)
plt.title('PRICE SEGMENTATION', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('outputs/price_segmentation.png', dpi=300, bbox_inches='tight')
plt.show()

# ============================================
# INSIGHT 5: RATING DISTRIBUTION
# ============================================
print("\n[6] Insight 5: Rating Distribution")

rating_counts = df['Rating'].value_counts().sort_index()
print("Rating Distribution:")
for rating, count in rating_counts.items():
    print(f"  • Rating {rating}: {count} menu")

plt.figure(figsize=(10, 5))
sns.barplot(x=rating_counts.index, y=rating_counts.values, palette="rocket")
plt.title('DISTRIBUTION OF MENU RATINGS', fontsize=14, fontweight='bold')
plt.xlabel('Rating')
plt.ylabel('Number of Menus')
plt.xticks(rotation=0)

# Add value labels on bars
for i, v in enumerate(rating_counts.values):
    plt.text(i, v + 0.5, str(v), ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.savefig('outputs/rating_distribution.png', dpi=300, bbox_inches='tight')
plt.show()

# ============================================
# SIMPLE SUMMARY
# ============================================
print("\n" + "=" * 50)
print("📈 SUMMARY STATISTICS:")
print("=" * 50)
print(f"• Total Menu Analyzed: {len(df):,}")
print(f"• Total Restaurants: {df['Nama_Tempat'].nunique()}")
print(f"• Average Price: Rp {df['Harga_Rata_Rata'].mean():,.0f}")
print(f"• Average Rating: {df['Rating'].mean():.2f}")
print(f"• Total Reviews Analyzed: {df['Jumlah_Ulasan_Menu'].sum():,}")

print("\n" + "=" * 50)
print("✅ ANALYSIS COMPLETE!")
print("✅ 5 visualizations saved to 'outputs' folder")
print("=" * 50)