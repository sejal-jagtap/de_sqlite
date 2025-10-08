import sqlite3
import pandas as pd

# Connect to the SQLite database (change path if Dbeaver is being used)
conn = sqlite3.connect("university_database.db")
cursor = conn.cursor()

# ---------------------------- Analysis Section ---------------------------- #

print("\n--- First 5 Records ---")
query = "SELECT * FROM university_rankings LIMIT 5;"
print(pd.read_sql_query(query, conn))

print("\n--- Total Number of Universities ---")
query = "SELECT COUNT(DISTINCT(institution)) AS number_of_universities FROM university_rankings;"
print(pd.read_sql_query(query, conn))

print("\n--- Total Number of Countries ---")
query = (
    "SELECT COUNT(DISTINCT(country)) AS number_of_countries FROM university_rankings;"
)
print(pd.read_sql_query(query, conn))

print("\n--- Top 5 Universities by Score (Latest Year) ---")
query = """
SELECT institution, country, score, year
FROM university_rankings
WHERE year = (SELECT MAX(year) FROM university_rankings)
ORDER BY score DESC
LIMIT 5;
"""
print(pd.read_sql_query(query, conn))

print("\n--- Bottom 5 Universities by Score (Latest Year) ---")
query = """
SELECT institution, country, score, year
FROM university_rankings
WHERE year = (SELECT MAX(year) FROM university_rankings)
ORDER BY score ASC
LIMIT 5;
"""
print(pd.read_sql_query(query, conn))

print("\n--- Average Score by Country ---")
query = """
SELECT country, ROUND(AVG(score), 2) AS avg_country_score
FROM university_rankings
GROUP BY country
ORDER BY avg_country_score DESC;
"""
print(pd.read_sql_query(query, conn))

print("\n--- Top University per Country ---")
query = """
WITH ranked_universities AS (
    SELECT country, institution, AVG(score) AS avg_score,
           ROW_NUMBER() OVER (PARTITION BY country ORDER BY AVG(score) DESC) AS rn
    FROM university_rankings
    GROUP BY country, institution
)
SELECT country, institution, ROUND(avg_score, 2) AS avg_score
FROM ranked_universities
WHERE rn = 1
ORDER BY country;
"""
print(pd.read_sql_query(query, conn))

print("\n--- Number of Universities in Top 100 by Country ---")
query = """
SELECT country, COUNT(DISTINCT institution) AS universities_in_top_100
FROM university_rankings
WHERE world_rank <= 100
GROUP BY country
ORDER BY universities_in_top_100 DESC;
"""
print(pd.read_sql_query(query, conn))

# ---------------------------- CRUD Section ---------------------------- #

print("\n--- Inserting a New University (Duke Tech) ---")
cursor.execute(
    """
INSERT INTO university_rankings (institution, country, world_rank, score, year)
VALUES ('Duke Tech', 'USA', 350, 60.5, 2014);
"""
)
conn.commit()

print("\n--- Verify Insert ---")
query = "SELECT institution, country, world_rank, score, year FROM university_rankings WHERE institution = 'Duke Tech';"
print(pd.read_sql_query(query, conn))

print("\n--- Top 200 Universities from Japan in 2013 ---")
query = """
SELECT COUNT(DISTINCT institution) AS top_200_japan_2013
FROM university_rankings
WHERE country = 'Japan' AND world_rank <= 200 AND year = 2013;
"""
print(pd.read_sql_query(query, conn))

print("\n--- Updating Oxford’s 2014 Score by +1.2 ---")
cursor.execute(
    """
UPDATE university_rankings
SET score = score + 1.2
WHERE institution = 'University of Oxford' AND year = 2014;
"""
)
conn.commit()

print("\n--- Verify Update ---")
query = "SELECT score, * FROM university_rankings WHERE institution = 'University of Oxford' AND year = 2014;"
print(pd.read_sql_query(query, conn))

print("\n--- Deleting Universities with Score < 45 in 2015 ---")
cursor.execute(
    """
DELETE FROM university_rankings
WHERE year = 2015 AND score < 45;
"""
)
conn.commit()

print("\n--- Verify Deletion ---")
query = "SELECT * FROM university_rankings WHERE year = 2015 AND score < 45;"
print(pd.read_sql_query(query, conn))

# ---------------------------------------------------------------------- #

conn.close()
print("\nAll queries executed successfully.")
