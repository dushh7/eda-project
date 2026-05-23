import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ==================================
# CREATE VISUALS FOLDER
# ==================================
os.makedirs("visuals", exist_ok=True)

# ==================================
# LOAD DATASET
# ==================================
df = pd.read_csv("data/dataset.csv")

# ==================================
# BASIC INFORMATION
# ==================================
print("\n===== FIRST 5 ROWS =====")
print(df.head())

print("\n===== DATASET INFO =====")
print(df.info())

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== STATISTICAL SUMMARY =====")
print(df.describe())

# ==================================
# REMOVE DUPLICATES
# ==================================
df = df.drop_duplicates()

# ==================================
# GRAPH 1 — MOVIES vs TV SHOWS
# ==================================
plt.figure(figsize=(8,5))

sns.countplot(x='type', data=df)

plt.title("Movies vs TV Shows")
plt.xlabel("Type")
plt.ylabel("Count")

plt.savefig("visuals/movies_vs_tvshows.png")

plt.close()

# ==================================
# GRAPH 2 — RELEASE YEAR TREND
# ==================================
plt.figure(figsize=(12,6))

df['release_year'].value_counts().sort_index().plot()

plt.title("Netflix Content Release Trend")
plt.xlabel("Release Year")
plt.ylabel("Number of Shows")

plt.savefig("visuals/release_year_trend.png")

plt.close()

# ==================================
# GRAPH 3 — TOP 10 COUNTRIES
# ==================================
top_countries = df['country'].dropna().value_counts().head(10)

plt.figure(figsize=(12,6))

top_countries.plot(kind='bar')

plt.title("Top 10 Countries Producing Netflix Content")
plt.xlabel("Country")
plt.ylabel("Count")

plt.savefig("visuals/top_countries.png")

plt.close()

# ==================================
# GRAPH 4 — CONTENT RATINGS
# ==================================
plt.figure(figsize=(10,6))

sns.countplot(
    y='rating',
    data=df,
    order=df['rating'].value_counts().index
)

plt.title("Netflix Ratings Distribution")

plt.savefig("visuals/ratings_distribution.png")

plt.close()

# ==================================
# GRAPH 5 — TOP GENRES
# ==================================
genres = df['listed_in'].str.split(', ', expand=True).stack()

top_genres = genres.value_counts().head(10)

plt.figure(figsize=(12,6))

top_genres.plot(kind='bar')

plt.title("Top 10 Genres on Netflix")
plt.xlabel("Genre")
plt.ylabel("Count")

plt.savefig("visuals/top_genres.png")

plt.close()

# ==================================
# GRAPH 6 — CONTENT ADDED OVER TIME
# ==================================
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

content_added = df['date_added'].dt.year.value_counts().sort_index()

plt.figure(figsize=(12,6))

content_added.plot()

plt.title("Content Added to Netflix Over Time")
plt.xlabel("Year")
plt.ylabel("Count")

plt.savefig("visuals/content_added_trend.png")

plt.close()

# ==================================
# FINAL INSIGHTS
# ==================================
print("\n===== KEY INSIGHTS =====")

print("1. Netflix contains more Movies than TV Shows.")
print("2. Content production increased rapidly after 2015.")
print("3. United States contributes the highest amount of content.")
print("4. TV-MA is the most common content rating.")
print("5. International Movies and Dramas dominate Netflix genres.")

print("\nAll graphs saved successfully in visuals folder!")