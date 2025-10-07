# 🏫 University Rankings — SQLite Project

## Overview  
This project explores a **global university ranking dataset** using SQL to uncover insights into institutional performance, international distribution, and ranking trends over time.  
All queries were executed in **SQLite**, using both **DBeaver** and **VS Code** for database management and analysis.

The project covers:
- Exploratory Data Analysis (EDA)
- CRUD (Create, Read, Update, Delete) operations
- Database updates and cleanup

## 📁 Project Structure

    de_sqlite/
    |-- README.md
    |-- query_results
    |-- sql_queries.sql
    `-- university_database.db
---

## ⚙️ Environment Setup

### Option 1 — Using **DBeaver**
1. Open DBeaver and click **Database → New Database Connection**.  
2. Select **SQLite** from the list of available database types.  
3. Choose your local `.db` file (e.g., `university_rankings.db`).  
4. Once connected, open a new **SQL Editor** and run the provided queries (`sql_queries.sql`).   
5. Explore data using the built-in Data tab to inspect record changes.

### Option 2 — Using **VS Code with SQLite**
1. Install the **SQLite** and **SQLTools** extensions in VS Code.  
2. Open your project folder (`de_sqlite`).  
3. Connect to the SQLite database file (`university_rankings.db`).  
4. Open the `.sql` file (e.g., `sql_queries.sql`) and run statements directly using **“Run Query”**.  
5. View results in the output panel or via the SQLTools results tab.  
6. Save changes automatically reflected in the same `.db` file.

---

## 🔍 Data Exploration Summary 
### 1. **Initial Dataset Inspection**
- Viewed the first few rows of the dataset to confirm column names and data integrity.  
- Counted the **total number of universities** and the **number of unique countries** represented.

<img width="750" height="600" alt="image" src="https://github.com/user-attachments/assets/307a2d6a-005d-41fa-a136-0f21894ce2ce" />

<img width="200" height="50" alt="image" src="https://github.com/user-attachments/assets/4ad2a0bb-e90b-4918-b2ed-f70fcb7c7cf7" />

<img width="200" height="50" alt="image" src="https://github.com/user-attachments/assets/afb94652-b569-4bc3-a5c9-50319d4fdcec" />

### 2. **Ranking Insights**
- Identified the **top 5 universities** by score in the **latest available year** to highlight leading institutions.  
- Retrieved the **bottom 5 universities** for the same year to understand the score range and data spread.

<img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/fd112898-2ad3-47c6-be2b-8cacb28d9ca7" />

<img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/a2936ca3-b826-414b-a00d-09566f91bcef" />

### 3. **Country-Level Analysis**
- Calculated the **average score per country**, rounding to two decimal places, to compare national performance.  
- Determined the **top-performing university in each country** based on average score across all available years.  
- Counted how many universities from each country ranked within the **global top 100**, providing a global competitiveness view.

<img width="600" height="450" alt="image" src="https://github.com/user-attachments/assets/65075be9-0a2d-447c-99b9-5b9fb1c1fcd4" />

<img width="600" height="450" alt="image" src="https://github.com/user-attachments/assets/c3f26434-62df-4f41-8199-d845bf64f8a8" />

<img width="600" height="450" alt="image" src="https://github.com/user-attachments/assets/e46da1c7-8630-4c7f-9cef-5629829d98f3" />

#### Note: For full result snapshots, please refer to the images in query_results/
---

## ⚙️ CRUD Operations

### 1. **CREATE: Adding a New University (2014)**  
- Inserted a new entry for **Duke Tech** (USA) with a **world rank of 350** and **score of 60.5** for **2014**.  
- Verified the new row by viewing 2014 rankings.

**Explanation:**  
- The `INSERT INTO` statement was used to add a new row.  
- All required columns (institution, country, world_rank, year, score) were populated.  
- The new entry was verified by querying all 2014 records and checking for the new institution.


<img width="838" height="78" alt="image" src="https://github.com/user-attachments/assets/94b34aaf-dba1-4c95-9f66-9acdb39209fe" />

### 2. **READ: Counting Japanese Universities in Top 200 (2013)**  
- Retrieved the total number of universities from **Japan** ranked within the **top 200** globally in **2013**.  
- This confirmed Japan’s representation among leading institutions that year.

**Explanation:**  
- Used a `SELECT COUNT(*)` query filtered by `country = 'Japan'`, `year = 2013`, and `world_rank <= 200`.  
- The result provides a numeric count rather than a list, summarizing Japan’s representation among the global elite that year.
  
<img width="265" height="73" alt="image" src="https://github.com/user-attachments/assets/d654369d-5f8d-49a8-bd2d-e55cd4f8b2d4" />

### 3. **UPDATE: Correcting University of Oxford’s Score (2014)**  
- Adjusted **University of Oxford’s** score for **2014**, increasing it by **+1.2 points** after a miscalculation was identified.  
- Verified the updated value reflected accurately in the dataset.

**Explanation:** 
- Used an `UPDATE` statement targeting the specific record with `institution = 'University of Oxford'` and `year = 2014`.  
- The `SET score = score + 1.2` expression incremented the existing score.  
- Verified the update by selecting the modified row and comparing the old and new scores.

<img width="1218" height="82" alt="image" src="https://github.com/user-attachments/assets/8af936c5-2950-467b-a627-4f080e5200e0" />

### 4. **DELETE: Removing Invalid 2015 Records**  
- Deleted all **2015** entries with scores **below 45**, as these universities should not have been included in the published rankings.  
- Confirmed the cleanup by verifying no remaining low-score entries in the 2015 data.

**Explanation:**  
- A `DELETE FROM` statement was used with the condition `WHERE year = 2015 AND score < 45`.  
- This removed only low-performing institutions from 2015, keeping all other data intact.  
- Verified deletion by checking that no remaining 2015 records had scores under 45.

<img width="1218" height="403" alt="image" src="https://github.com/user-attachments/assets/aa047b21-65be-48d5-bc70-a288de10de16" />

---

## 🧠 Results & Observations
- The majority of top-ranked universities were consistently from the **USA** and **UK**.  
- Japan, China, and Germany had a growing presence in mid-tier global rankings.  
- After cleaning, the dataset reflected only globally competitive institutions for 2015.  

---







