import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =========================================
# LOAD DATASET
# =========================================

df = pd.read_csv("/Users/potlurubhavithmadhu/Desktop/Python/Netfilx_Clone/netflix_titles.csv")
print("========== FIRST 5 ROWS ==========")
print(df.head())

# =========================================
# BASIC INFO
# =========================================

print("\n========== DATASET INFO ==========")
print(df.info())

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# =========================================
# MOST COMMON CONTENT TYPE
# =========================================

print("\n========== CONTENT TYPES ==========")

print(df["type"].value_counts())

# =========================================
# MOVIES VS TV SHOWS BAR GRAPH
# =========================================

sns.countplot(x="type", data=df)

plt.title("Movies vs TV Shows")

plt.show()

# =========================================
# TOP 10 COUNTRIES
# =========================================

top_countries = df["country"].value_counts().head(10)

print("\n========== TOP COUNTRIES ==========")
print(top_countries)

# BAR GRAPH

top_countries.plot(kind="bar")

plt.title("Top 10 Countries on Netflix")

plt.xlabel("Country")
plt.ylabel("Count")

plt.show()

# =========================================
# RELEASE YEAR ANALYSIS
# =========================================

release_years = df["release_year"].value_counts().head(10)

print("\n========== MOST COMMON RELEASE YEARS ==========")

print(release_years)

# =========================================
# RATINGS DISTRIBUTION
# =========================================

plt.figure(figsize=(10,5))

sns.countplot(y="rating", data=df,
              order=df["rating"].value_counts().index)

plt.title("Ratings Distribution")

plt.show()

# =========================================
# MOVIES ONLY
# =========================================

movies = df[df["type"] == "Movie"]

print("\n========== MOVIES DATA ==========")
print(movies.head())

# =========================================
# TV SHOWS ONLY
# =========================================

tv_shows = df[df["type"] == "TV Show"]

print("\n========== TV SHOWS DATA ==========")
print(tv_shows.head())

# =========================================
# TOP 10 DIRECTORS
# =========================================

top_directors = df["director"].value_counts().head(10)

print("\n========== TOP DIRECTORS ==========")

print(top_directors)

# =========================================
# HISTOGRAM OF RELEASE YEARS
# =========================================

plt.hist(df["release_year"], bins=20)

plt.title("Distribution of Release Years")

plt.xlabel("Year")
plt.ylabel("Count")

plt.show()

print("\n========== PROJECT COMPLETED ==========")