# 🏫 University Rankings — SQLite Project

## Overview  
This project explores a **global university ranking dataset** using SQL to uncover insights into institutional performance, international distribution, and ranking trends over time.  
All queries were executed in **SQLite**, using both **DBeaver** and **VS Code** for database management and analysis.

The project covers:
- Exploratory Data Analysis (EDA)
- CRUD (Create, Read, Update, Delete) operations
- Database updates and cleanup
  
---

## 🔍 Data Exploration Summary  
### 1. **Initial Dataset Inspection**
- Viewed the first few rows of the dataset to confirm column names and data integrity.  
- Counted the **total number of universities** and the **number of unique countries** represented.

<img width="500" height="200" alt="image" src="https://github.com/user-attachments/assets/307a2d6a-005d-41fa-a136-0f21894ce2ce" />


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

<img width="500" height="350" alt="image" src="https://github.com/user-attachments/assets/65075be9-0a2d-447c-99b9-5b9fb1c1fcd4" />
<img width="500" height="350" alt="image" src="https://github.com/user-attachments/assets/00587dde-8c20-46f4-a073-b7e6a35a8d42" />
<img width="500" height="350" alt="image" src="https://github.com/user-attachments/assets/01da7688-8f78-43e7-b219-f2490deea7fc" />

--------------------------------------------------------------------------------------------------------------------

<img width="500" height="350" alt="image" src="https://github.com/user-attachments/assets/c3f26434-62df-4f41-8199-d845bf64f8a8" />
<img width="500" height="350" alt="image" src="https://github.com/user-attachments/assets/20d1206e-f9b5-4364-b93c-489413c9673c" />
<img width="500" height="350" alt="image" src="https://github.com/user-attachments/assets/38f4dc88-48c1-4e2c-8328-056291d6f2d1" />

-------------------------------------------------------------------------------------------------------------------

<img width="500" height="350" alt="image" src="https://github.com/user-attachments/assets/e46da1c7-8630-4c7f-9cef-5629829d98f3" />

---

## ⚙️ CRUD Operations

### 1. **CREATE: Adding a New University (2014)**  
- Inserted a new entry for **Duke Tech** (USA) with a **world rank of 350** and **score of 60.5** for **2014**.  
- Verified the new row by viewing 2014 rankings.

### 2. **READ: Counting Japanese Universities in Top 200 (2013)**  
- Retrieved the total number of universities from **Japan** ranked within the **top 200** globally in **2013**.  
- This confirmed Japan’s representation among leading institutions that year.

### 3. **UPDATE: Correcting University of Oxford’s Score (2014)**  
- Adjusted **University of Oxford’s** score for **2014**, increasing it by **+1.2 points** after a miscalculation was identified.  
- Verified the updated value reflected accurately in the dataset.

### 4. **DELETE: Removing Invalid 2015 Records**  
- Deleted all **2015** entries with scores **below 45**, as these universities should not have been included in the published rankings.  
- Confirmed the cleanup by verifying no remaining low-score entries in the 2015 data.

---

## 🧠 Results & Observations
- The majority of top-ranked universities were consistently from the **USA** and **UK**.  
- Japan, China, and Germany had a growing presence in mid-tier global rankings.  
- After cleaning, the dataset reflected only globally competitive institutions for 2015.  

---

## ⚙️ Environment Setup

### Option 1 — Using **DBeaver**
1. Open DBeaver and click **Database → New Database Connection**.  
2. Select **SQLite** from the list of available database types.  
3. Choose your local `.db` file (e.g., `university_rankings.db`).  
4. Once connected, open a new **SQL Editor** and run the provided queries (`sql_queries.sql`).   
5. Explore data using the built-in Data tab to visually inspect table changes.

### Option 2 — Using **VS Code with SQLite**
1. Install the **SQLite** and **SQLTools** extensions in VS Code.  
2. Open your project folder (`de_sqlite`).  
3. Connect to the SQLite database file (`university_rankings.db`).  
4. Open the `.sql` file (e.g., `sql_queries.sql`) and run statements directly using **“Run Query”**.  
5. View results in the output panel or via the SQLTools results tab.  
6. Save changes automatically reflected in the same `.db` file.

---

## 📁 Project Structure


