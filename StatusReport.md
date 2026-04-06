
## 1. Project Overview

Our project investigates whether or not economic conditions, such as unemployment rates are associated with crime rates across U.S. states. Our core approach and research question from the Project Plan is the same. The only big update we made is that we replaced the originally planned data with two cleaner and more compatible datasets. Here they are:

- **Dataset 1 (Crime):** FBI UCR State Crime dataset sourced from the FBI's Uniform Crime Reporting Statistics page, covering all 50 U.S. states + D.C., years 1960–2019.
- **Dataset 2 (Unemployment):** USDA Economic Research Service (ERS) County-Level Data Set — *Unemployment and Median Household Income for the United States, States, and Counties, 2000–2023.* Unemployment rates are derived from BLS LAUS; median household income from Census Bureau SAIPE.

We did this, because the ERS dataset has both state-level and county-level records in a single, file and also includes median household income as a bonus variable, which will strengthen our analysis. Both datasets are published by federal agencies and are publicly available.
Our analysis is now state-level (rather than county-level) because the FBI UCR dataset in its current form is organized by state. The overlapping years between the two datasets are 2000–2019, giving us 20 years × 51 jurisdictions = 1,020 integrated records.



## 2. Task-by-Task Status Update

| Task | Responsible | Original Target | Status | Notes |
|---|---|---|---|---|
| Data Acquisition | Arjun | Week 2 | Done | Both datasets downloaded; uploaded to `data/raw/` in repo |
| Data Cleaning | Kishan | Week 3 | Done | See `clean_and_merge.py` and Section 4 below |
| Data Integration | Arjun | Week 3 | Done | Merged dataset at `data/processed/merged_crime_unemployment.csv` |
| Exploratory Data Analysis | Kishan | Week 4 | In Progress | Descriptive stats and correlations completed; visualizations pending |
| Visualization | Arjun | Week 4 | In Progress | Scatter plots and trend lines planned for next week |
| Statistical Analysis | Both | Week 5 | Not Started Yet | Correlation and regression analysis upcoming |
| Documentation & Report | Both | Week 5 | Not Started Yet | Will begin after analysis is complete |

---

## 3. Updated Timeline

| Task | Responsible | Deadline | Status |
|---|---|---|---|
| Data Acquisition | Arjun | Week 2 (completed) | Done |
| Data Cleaning & Integration | Kishan + Arjun | Week 3 (completed) | Done |
| Exploratory Data Analysis | Kishan | April 12, 2026 | In Progress |
| Visualization | Arjun | April 19, 2026 | In Progress |
| Statistical Analysis (correlation + regression) | Both | April 26, 2026 | Upcoming |
| Final Report (README.md) | Both | May 3, 2026 | Upcoming |
| Final Submission & GitHub Release | Both | May 5, 2026 | Upcoming |

---

## 4. Data Lifecycle and Artifacts

### 4.1 Data Sources

**Dataset 1 — FBI UCR State Crime**  
- Source: [https://ucr.fbi.gov/crime-in-the-u.s](https://ucr.fbi.gov/crime-in-the-u.s)  
- File: `data/raw/state_crime.csv`  
- Coverage: 50 U.S. states + D.C., years 1960–2019  
- Format: CSV, 3,115 rows × 21 columns (before filtering)  
- Key variables: `State`, `Year`, violent and property crime rates per 100,000 population, total crime counts

**Dataset 2 — USDA ERS Unemployment and Median Household Income**  
- Source: [https://www.ers.usda.gov/data-products/county-level-data-sets/county-level-data-sets-download-data](https://www.ers.usda.gov/data-products/county-level-data-sets/county-level-data-sets-download-data)  
- File: `data/raw/Unemployment2023.csv`  
- Coverage: All U.S. counties and states, years 2000–2023  
- Format: CSV (long/tidy format), 329,726 rows × 5 columns (before reshaping)  
- Key variables: `FIPS_Code`, `State`, `Area_Name`, `Attribute` (metric + year encoded), `Value`

### 4.2 Data Cleaning Summary

We use our python script:  clean_and_merge.py. to clean and merge our data.

**Crime dataset:**
- We renamed 19 columns from dot-notation ( Data.Rates.Violent.All) to snake_case ( violent_crime_rate) for readability.
- We removed the "United States" national aggregate row, keeping only state observations.
- We filtered rows to 2000–2019 to match the unemployment data's available range.
- And then we didn’t find any missing values in any column.

**Unemployment dataset:**
- We filtered to state-level records using FIPS codes divisible by 1,000 (excluding FIPS = 0, the U.S. national aggregate).
- We parsed the year and metric name out of the encoded `Attribute` column using regular expressions (e.g., `Unemployment_rate_2009` → year = 2009, metric = `Unemployment_rate`).
- We pivoted from long to wide format so each row represents one state-year observation.
- We mapped two-letter state abbreviations to full state names to enable joining with the crime dataset.
- We filtered to 2000–2019.
- And then we didn’t find any missing values in any column.

### 4.3 Data Integration

We merged the two cleaned datasets on State and Year using an inner join. From the unemployment dataset, the  columns we retained for the final merged file were: Unemployment_rate, Civilian_labor_force, Employed, Unemployed, and Median_Household_Income.

**Merged dataset:** `data/processed/merged_crime_unemployment.csv`  
- Shape: **1,020 rows × 22 columns**  
- Jurisdictions: 51 (50 states + D.C.)  
- Years: 2000–2019  
- Missing values: **0**

### 4.4 Data Quality Assessment

| Dimension | Crime Dataset | Unemployment Dataset | Merged Dataset |
|---|---|---|---|
| Completeness | No missing values | No missing values | No missing values |
| Coverage | 51 jurisdictions, 2000–2019 (after filter) | 51 jurisdictions, 2000–2019 (after filter) | 51 × 20 = 1,020 records |
| Consistency | Column names standardized | Long-to-wide reshape applied; state abbrevs mapped | Inner join produced no unmatched records |
| Outliers | Max violent crime rate = 1,637.9 (DC, expected) | Max unemployment = 13.8% (Nevada 2010, expected post-2008) | Outliers are real, not errors |

Outlier review: The highest violent crime rate belongs to the District of Columbia. The highest unemployment values correspond to Nevada and Michigan during 2009–2011, which shows the impact of the 2008 financial crisis, both expected and valid observations.

### 4.5 Preliminary Findings

Descriptive statistics of key variables (1,020 state-year observations):

| Variable | Mean | Std | Min | Max |
|---|---|---|---|---|
| `violent_crime_rate` (per 100k) | 404.2 | 208.3 | 78.2 | 1,637.9 |
| `property_crime_rate` (per 100k) | 2,985.3 | 877.0 | 1,179.8 | 6,409.0 |
| `Unemployment_rate` (%) | 5.51 | 2.01 | 2.1 | 13.8 |

Preliminary Pearson correlations:

| Variable Pair | Correlation |
|---|---|
| Violent crime rate × Unemployment rate | **+0.215** |
| Property crime rate × Unemployment rate | **+0.072** |
| Violent crime rate × Property crime rate | **+0.609** |

A positive correlation between unemployment and violent crime is present, though modest, which motivates the planned regression analysis to control for additional variables.

---

## 5. Ethical and Legal Considerations

Both datasets are published by U.S. federal agencies (FBI and USDA/BLS/Census Bureau) and are in the **public domain**. No personally identifiable information is present — data is aggregated at the state level. No consent or privacy issues apply. Both datasets are freely redistributable.

---

## 6. Challenges and Resolutions

**Challenge 1 — Dataset format mismatch (long vs. wide)**  
The unemployment dataset uses a long/tidy format where each row encodes a single metric-year combination in a text field. Joining this directly to the crime dataset required parsing the year and metric from the `Attribute` column and pivoting to wide format. This was resolved using regular expressions and `pandas.pivot_table`.

**Challenge 2 — State identifier mismatch**  
The crime dataset uses full state names while the unemployment dataset uses two-letter FIPS-based abbreviations. This was resolved by creating a lookup dictionary mapping abbreviations to full names before the merge.

**Challenge 3 — Scale difference (county vs. state)**  
The original plan called for county-level analysis, but the FBI UCR dataset in the available format is organized at the state level. We adjusted the project scope to state-level analysis, which actually improves consistency between the two datasets and eliminates the risk of county identifier mismatches.

**Challenge 4 — Year range overlap**  
The crime dataset covers 1960–2019 and the unemployment dataset covers 2000–2023. The overlapping window of 2000–2019 limits the time span to 20 years, which is sufficient for meaningful trend analysis but reduces the historical depth originally envisioned.

---

## 7. Individual Contribution Summaries

### Arjun
I was responsible for data acquisition and integration. I located and downloaded both final datasets from the USDA ERS and FBI UCR portals and verified their integrity. I then wrote the merging logic in clean_and_merge.py, handling the FIPS-based filtering for state-level records and the inner join on State + Year. I also conducted the preliminary correlation analysis and drafted Sections 1, 4.3, and 4.5 of this status report.

### Kishan
I handled data cleaning for both datasets. For the crime dataset, I standardized column names and removed the national aggregate row. For the unemployment dataset, I wrote the regex-based parsing logic to extract year and metric from the Attribute column and implemented the pivot to wide format. I documented the data quality assessment (Section 4.4), drafted the challenges section, and reviewed the integration output for consistency. I also drafted Sections 4.1, 4.2, and 6 of this report.

---

## 8. References

- Federal Bureau of Investigation. *Crime in the United States* (UCR Program). [https://ucr.fbi.gov/crime-in-the-u.s](https://ucr.fbi.gov/crime-in-the-u.s)
- USDA Economic Research Service. *Unemployment and Median Household Income for the United States, States, and Counties, 2000–23.* [https://www.ers.usda.gov/data-products/county-level-data-sets/](https://www.ers.usda.gov/data-products/county-level-data-sets/)
- U.S. Bureau of Labor Statistics. *Local Area Unemployment Statistics (LAUS).* [https://www.bls.gov/lau/](https://www.bls.gov/lau/)
- U.S. Census Bureau. *Small Area Income and Poverty Estimates (SAIPE).* [https://www.census.gov/programs-surveys/saipe.html](https://www.census.gov/programs-surveys/saipe.html)
