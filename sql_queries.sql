
/* ---------------------------------------- Analysis ------------------------------------------------------- */

/* View first 5 */
SELECT *
FROM university_rankings
LIMIT 5;

/* Count total universities */
SELECT count(distinct(institution)) as number_of_universities
FROM university_rankings;

/* Count total universities */
SELECT count(distinct(country)) as number_of_countries
FROM university_rankings;

/* Top 5 universities by score in the latest year */
SELECT institution, country, score, year
FROM university_rankings
WHERE year = (SELECT MAX(year) FROM university_rankings)
ORDER BY score DESC
LIMIT 5;

/* Bottom 5 universities by score in the latest year */
SELECT institution, country, score, year
FROM university_rankings
WHERE year = (SELECT MAX(year) FROM university_rankings)
ORDER BY score ASC
LIMIT 5;

/* Average score by country */
SELECT 
    country, 
    ROUND(AVG(score), 2) AS avg_country_score
FROM university_rankings
GROUP BY country
ORDER BY avg_country_score DESC;

/* Top university per country */
WITH ranked_universities AS (
    SELECT
        country,
        institution,
        AVG(score) AS avg_score,
        ROW_NUMBER() OVER (
            PARTITION BY country
            ORDER BY AVG(score) DESC
        ) AS rn
    FROM university_rankings
    GROUP BY country, institution
)
SELECT country, institution, ROUND(avg_score, 2) AS avg_score
FROM ranked_universities
WHERE rn = 1
ORDER BY country;

/* Number of universities in top 100 by country */
SELECT country, COUNT(DISTINCT institution) AS universities_in_top_100
FROM university_rankings
WHERE world_rank <= 100
GROUP BY country
ORDER BY universities_in_top_100 DESC;

/* ---------------------------------------- CRUD Operations ------------------------------------------------------- */


INSERT INTO university_rankings (institution, country, world_rank, score, year)
VALUES ('Duke Tech', 'USA', 350, 60.5, 2014);

SELECT institution, country, world_rank, score, year
FROM university_rankings
WHERE institution = 'Duke Tech';

SELECT COUNT(DISTINCT institution ) AS top_200_japan_2013
FROM university_rankings
WHERE country = 'Japan'
AND world_rank <= 200
AND year = 2013;

UPDATE university_rankings
SET score = score + 1.2
WHERE institution  = 'University of Oxford'
AND year = 2014;

SELECT score,* 
FROM university_rankings 
WHERE institution  = 'University of Oxford'
AND year = 2014;

DELETE FROM university_rankings
WHERE year = 2015
AND score < 45;

SELECT * 
FROM university_rankings 
WHERE year = 2015 
AND score < 45;



