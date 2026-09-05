# layoff_project
Data cleaning, validation, and exploratory analysis of 1,900+ global tech workforce reduction events using Python and pandas.
# Tech Layoffs Data Cleaning & Exploratory Analysis

## Project Overview
Between 2020 and 2023, macroeconomic headwinds led to significant workforce reductions across the technology sector. This project focuses on building an automated data cleaning and exploratory analysis pipeline using Python and pandas. The raw dataset contained issues such as duplicate records, missing impact metrics, split category labels, and string inconsistencies.

## Key Objectives
- Audit raw layoff records for structural integrity and missingness.
- Remove duplicate rows and filter out records with no measurable impact data.
- Standardize categorical labels and strip whitespace inconsistencies.
- Perform exploratory aggregations to identify top impacted regions, industries, and enterprises.

---

## Tech Stack
- **Language:** Python
- **Libraries:** pandas, NumPy
- **Environment:** Jupyter Notebook / Python Script

---

## Data Cleaning Workflow
1. **Deduplication:** Dropped exact duplicate rows across all fields using `.drop_duplicates()`.
2. **Handling Unusable Records:** Removed rows missing both `total_laid_off` and `percentage_laid_off` using `.dropna(subset=[...], how='all')`.
3. **Categorical Standardization:** 
   - Unified variations of cryptocurrency classifications (`Crypto Currency`, `CryptoCurrency`) into a single standard label: `Crypto`.
   - Stripped trailing punctuation artifacts in geographical entries (e.g., standardizing `United States.` to `United States`).
4. **Whitespace Trimming:** Applied `.str.strip()` to string columns (`company`, `country`) to prevent silent grouping errors.
5. **Export:** Exported the verified 1,995-row dataset to `layoffs_cleaned.csv`.

---

## Key Insights
- **Total Headcount Impact:** Over **383,600+ workforce reductions** documented across 1,995 events.
- **Top 5 Countries by Layoffs:**
  1. United States: 256,559
  2. India: 35,993
  3. Netherlands: 17,220
  4. Sweden: 11,264
  5. Brazil: 10,391
- **Top 5 Impacted Industries:**
  1. Consumer: 44,782
  2. Retail: 43,613
  3. Other: 36,289
  4. Transportation: 31,248
  5. Finance: 28,344
- **Largest Single-Company Layoff Counts:** Enterprise tech companies accounted for the largest individual cuts, led by Amazon (18,150), Google (12,000), Meta (11,000), Salesforce (10,090), and Microsoft (10,000).

---

## Repository Structure
```text
├── layoffs.csv                 # Raw dataset
├── layoffs_cleaning_2.py       # Python cleaning & aggregation script
├── layoffs_cleaned.csv         # Cleaned output dataset
└── README.md                   # Project documentation
