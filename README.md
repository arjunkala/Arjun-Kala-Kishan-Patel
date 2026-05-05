# Unemployment and Crime Rates Across U.S. States (2000–2019)

## Contributors

- Kishan Patel - Kpate514
- Arjun Kala - kala


## Summary

Our project takes a closer look at a question people have been asking for decades, which is "when the economy struggles, does crime go up?" More specifically, we examine whether state level unemployment rates are linked to crime rates across the United States from 2000 to 2019. Our idea for this came from a well known theory in criminology that economic hardship can push some individuals toward criminal activity, especially property-related crimes. To explore this, we combined two major public datasets: the FBI’s Uniform Crime Reporting data and unemployment estimates from the USDA’s Economic Research Service. This gave us a 20 year dataset covering all 50 states plus Washington, D.C., tracking both violent and property crime alongside annual unemployment levels.

Our results were that we found a relationship, but not a particularly strong one. Unemployment is statistically significantly associated with both violent crime (r = 0.215, p < 0.0001) and property crime (r = 0.186, p < 0.0001), which means there is a measurable connection. However, the strength of that relationship is relatively modest. When we ran regression models controlling for population, unemployment explained only about 5% of the variation in violent crime and about 3.5% in property crime. In other words, while unemployment does matter, it clearly isn’t the main driver behind changes in crime rates. Most of the variation is being influenced by other factors that aren’t captured in our dataset, so maybe things like policing strategies, demographic shifts, policy changes, or just broader social dynamics.
One of the most interesting takeaways we had came from looking at trends over time. Property crime steadily declined over the entire period, dropping from around 3,600 incidents per 100,000 people in 2000 to about 2,140 in 2019. What makes this especially notable is that this decline continued even during the Great Recession, when unemployment spiked dramatically between 2008 and 2010. If unemployment were a dominant driver of crime, we might expect crime rates to rise during that period, however they didn’t. This disconnect suggests that the relationship between economic conditions and crime is more complex than the traditional thoughts that most have, and that broader structural or societal factors are likely playing a much larger role than unemployment alone.



## Data Profile

### Dataset 1: FBI Uniform Crime Reporting — State Crime

**Source:** Marshall University's compiled UCR dataset, derived from the FBI Uniform Crime Reports  
**Access method:** CSV file download  
**Format:** Tabular CSV  
**Temporal coverage:** 1960–2019  
**Spatial coverage:** All 50 U.S. states and Washington D.C.  
**File location in repository:** `data/raw/state_crime.csv`  


The dataset contains annual state-level crime counts and rates (per 100,000 population) for both violent and property crime categories. After renaming columns for clarity and filtering to 2000–2019 and excluding the national "United States" aggregate row, the working dataset contained 1,020 records across 51 jurisdictions.

**Columns used:**

| Column | Description | Units |
|---|---|---|
| State | State name | String |
| Year | Year of observation | Integer |
| population | Estimated resident population | Count |
| violent_crime_rate | Total violent crimes per 100,000 | Rate |
| property_crime_rate | Total property crimes per 100,000 | Rate |
| burglary_rate | Burglaries per 100,000 | Rate |
| larceny_rate | Larcenies per 100,000 | Rate |
| motor_theft_rate | Motor vehicle thefts per 100,000 | Rate |
| assault_rate | Aggravated assaults per 100,000 | Rate |
| murder_rate | Murders per 100,000 | Rate |
| rape_rate | Rapes per 100,000 | Rate |
| robbery_rate | Robberies per 100,000 | Rate |

**Ethical and legal constraints:** The FBI UCR data is a public government dataset with no restrictions on reuse. Crime statistics represent reported crimes only.  So unreported crimes, changes in reporting practices over time, and variation in definitions across jurisdictions are known limitations of UCR data. The data contains no personally identifiable information.

**Relation to research question:** Provides the dependent variables (crime rates) across the full study period.


### Dataset 2: USDA ERS — County-Level Unemployment and Income Data

**Source:** USDA Economic Research Service (ERS)  
**Access method:** CSV file download  
**Format:** Long-format tabular CSV with an `Attribute` column encoding year and metric  
**Temporal coverage:** Multiple years including 2000–2019  
**Spatial coverage:** All U.S. counties and states (identified by FIPS code)  
**File location in repository:** `data/Unemployment2023.csv`  


The raw dataset is in a long format where each row represents a state or county × attribute × year combination. State-level records were isolated by filtering FIPS codes that are multiples of 1,000 (and nonzero), which is the standard convention for state-level FIPS aggregates. The long-format data was then pivoted to wide format, yielding one row per state per year with columns for each metric. The dataset originally has `Median_Household_Income`, `Civilian_labor_force`, `Employed`, and `Unemployed` alongside the unemployment rate, however our merged dataset used for analysis retains the unemployment rate only. 

**Columns used in merge:**

| Column | Description | Units |
|---|---|---|
| State | Full state name (mapped from abbreviation) | String |
| Year | Year of observation | Integer |
| Unemployment_rate | Annual average unemployment rate | Percent |

**Ethical and legal constraints:** This is a public dataset produced by a U.S. federal agency and is not subject to copyright restrictions. No personally identifiable information is present. One consideration is that county level data was aggregated to the state level, which may smooth over significant within state variation in unemployment and economic conditions.

**Relation to research question:** Provides the primary independent variable (unemployment rate) across the study period.


### Integration

The two datasets were merged on the composite key `(State, Year)` using an inner join in pandas. State abbreviations in the unemployment data were mapped to full state names to match the crime dataset's naming convention. The final merged dataset contains 1,020 rows (51 states × 20 years) with zero missing values across all retained columns.

**Merged file location:** `data/merged_crime_unemployment.csv`


## Data Quality

**Crime dataset:** After filtering to 2000–2019 and removing the U.S.-aggregate row, the crime data contained no missing values across any retained column. All rate values were positive and within plausible ranges. The maximum violent crime rate (1,637.9 per 100,000) belongs to Washington D.C., which is an extreme outlier due to its unique geographic and demographic characteristics as a single urban jurisdiction rather than a mixed urban/rural state, this was expected however, and documented, not a data error.

**Unemployment dataset:** The raw data required restructuring from long to wide format before quality could be assessed. After pivoting, no missing values were present for the `Unemployment_rate` column across the 2000–2019 window for any of the 51 matched jurisdictions. Values range from 2.1% to 13.8%, which is consistent with known macroeconomic conditions across this period (notably, values near 13% correspond to post-2008 recession years in hard-hit states).

**Merged dataset summary statistics:**

| Variable | Mean | Std Dev | Min | Max |
|---|---|---|---|---|
| violent_crime_rate | 404.2 | 208.3 | 78.2 | 1637.9 |
| property_crime_rate | 2985.3 | 877.0 | 1179.8 | 6409.0 |
| Unemployment_rate | 5.51% | 2.01% | 2.1% | 13.8% |
| population | 6,022,787 | 6,773,744 | 493,754 | 39,557,045 |

No duplicate state-year combinations were detected. No imputation was required.



## Data Cleaning

**Crime data:**
- Column names were renamed from dot notation format (e.g., `Data.Rates.Violent.All`) to snake_case (e.g., `violent_crime_rate`) to improve readability and compatibility.
- The aggregate "United States" row was dropped, as it is not a state-level observation and would inflate correlations.
- Records outside 2000–2019 were filtered out to align with the unemployment data's available range and to focus on a consistent modern period.

**Unemployment data:**
- Records were filtered to state-level FIPS codes (multiples of 1,000, excluding 0) to exclude county rows.
- Year and metric were extracted from the `Attribute` column using regular expressions (e.g., `"Unemployment_rate_2010"` → year `2010`, metric `Unemployment_rate`).
- The long-format table was pivoted to wide format with `pivot_table()`, producing one row per state per year.
- State abbreviations (e.g., `"IL"`) were mapped to full names (e.g., `"Illinois"`) using a manually constructed lookup dictionary to enable joining with the crime dataset.
- Records outside 2000–2019 were filtered to match the crime data.

**No values were imputed.** All cleaning operations were deterministic and are fully reproducible using our code in the python file: `clean_and_merge.py`.



## Findings

**Correlation analysis:**

Unemployment rate shows a statistically significant positive association with both crime types:

| Pair | Pearson r | p-value |
|---|---|---|
| Unemployment ↔ Violent crime | 0.215 | < 0.0001 |
| Unemployment ↔ Property crime | 0.186 | < 0.0001 |
| Violent crime ↔ Property crime | 0.609 | < 0.0001 |

The strong correlation between the two crime types (r = 0.609) suggests they share common underlying drivers beyond unemployment alone.

**Regression analysis:**

OLS regression with unemployment rate and log-transformed population as predictors explains only 4.7% of variance in violent crime (R² = 0.047) and 3.5% in property crime (R² = 0.035). While unemployment is a statistically significant predictor in both models (p < 0.0001), population is not (p = 0.44 for violent, p = 0.70 for property). The low R² values are the key finding, so unemployment is significantly but weakly associated with crime, meaning the majority of variation is driven by factors outside this model.

**Temporal trends (Figures 1 & 3):**

Property crime declined steadily across the full period, from a mean of 3,609 per 100,000 in 2000 to 2,141 in 2019 (a 41% drop) independent of unemployment fluctuations. Violent crime declined more modestly from 443 in 2000 to 379 in 2019. Unemployment spiked sharply from ~4.4% in 2007 to ~8.8% by 2010 during the financial crisis, then declined through 2019 to 3.6%. Notably, crime rates continued declining through the recession period rather than rising, which challenges a straightforward economic strain interpretation.

**Geographic variation (Figure 4):**

The District of Columbia, New Mexico, Alaska, Tennessee, and South Carolina had the highest average violent crime rates over 2000–2019. Maine, Vermont, New Hampshire, North Dakota, and Utah had the lowest. This geographic variation is substantial and likely reflects structural factors such as urbanization, poverty concentration, policing resources, not just captured by unemployment alone.



## Future Work

The most significant limitation of this project is the reliance on state level aggregates, which masks considerable within state variation. Future work should use county level data, which would substantially increase statistical power and allow for more granular geographic analysis. Incorporating additional socioeconomic controls such as poverty rates, educational attainment, incarceration rates, and demographic composition, would improve model specification and likely increase explanatory power well beyond the current R² of ~5%.

The project's time frame (2000–2019) was chosen deliberately to avoid pandemic-era distortions, but extending analysis to 2020–2023 would allow examination of an unusual natural experiment: how did crime respond to the sudden unemployment shock of COVID-19 compared to the more gradual 2008 recession?

A panel data approach using fixed effects, so controlling for time-invariant state characteristics would be a more appropriate modeling strategy than pooled OLS. The current approach treats each state-year as an independent observation, which it is not.

Finally, the project could be extended to examine specific crime subcategories. The data contains rates for burglary, larceny, motor vehicle theft, assault, murder, rape, and robbery separately. Theory predicts unemployment should be more strongly related to economically motivated crimes (burglary, robbery) than to crimes of passion or violence, and testing this would be a more theoretically grounded analysis.



## Challenges

**Data format mismatch:** The unemployment data was in a long format with year and metric encoded in a single `Attribute` string column, requiring regex-based parsing and a pivot operation before it could be joined with the crime data. This was the most technically demanding part of the integration.

**State name standardization:** The unemployment data used two-letter abbreviations while the crime data used full names. A manual mapping dictionary was required; any state omitted from this dictionary would silently drop rows from the merge. This was verified by confirming 51 states matched in the final dataset.

**D.C. as an outlier:** Washington D.C.'s violent crime rate (mean 1,334 per 100,000 — more than 3× the next highest state) creates leverage in the OLS models. It was retained because it is a legitimate jurisdiction in both source datasets, but its influence should be noted when interpreting regression coefficients.


## Reproducing This Project

1. Clone the repository:
   ```
   git clone https://github.com/[your-repo-url]
   cd [repo-name]
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Place raw data files in `data/raw/`:
   - `data/raw/state_crime.csv` — FBI UCR state crime data
   - `data/raw/Unemployment2023.csv` — USDA ERS unemployment data

4. Run the cleaning and merging script:
   ```
   python clean_and_merge.py
   ```
   This produces:
   - `data/processed/crime_clean.csv`
   - `data/processed/unemployment_clean.csv`
   - `data/processed/merged_crime_unemployment.csv`

5. Run the analysis script:
   ```
   python analyze.py
   ```
   This produces all figures in `results/figures/` and result tables in `results/`.


## References

- Federal Bureau of Investigation. *Uniform Crime Reports*, compiled by Marshall University. Available at: https://ucr.fbi.gov/crime-in-the-u.s 
- USDA Economic Research Service. *Unemployment and Median Household Income for the U.S., States, and Counties, 2000–2023*. Available at: https://www.ers.usda.gov/data-products/county-level-data-sets/county-level-data-sets-download-data
- McKinney, W. (2010). Data structures for statistical computing in Python. *Proceedings of the 9th Python in Science Conference*.
- Seabold, S. & Perktold, J. (2010). statsmodels: Econometric and statistical modeling with Python. *Proceedings of the 9th Python in Science Conference*.
- Virtanen, P. et al. (2020). SciPy 1.0: fundamental algorithms for scientific computing in Python. *Nature Methods*, 17, 261–272.
