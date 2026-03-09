The easiest way to succeed on this assignment is to **pick datasets that:**

- Come from **reliable sources (.gov or research institutions)**
- Have a **shared identifier** (county, state, year, etc.)
- Require **some cleaning and merging** (so your professor sees data wrangling)

Below is a **very strong project idea + datasets + analysis plan** you can use.

# **Project Idea (Simple but Strong)**

## **Topic**

**How do economic conditions affect crime rates across U.S. counties?**

This works very well because:

- Lots of **reliable government datasets**
- Easy to **merge by county FIPS code**
- Clear **business/policy question**
- Good for visualization and analysis

# **Research Questions**

You could use these in your plan.

**Primary Question**

How do economic indicators such as unemployment and income levels relate to crime rates across U.S. counties?

**Secondary Questions**

- Do counties with higher unemployment rates experience higher violent crime rates?
- Is median household income negatively correlated with crime rates?
- Are economic indicators better predictors of crime than population size?

# **Dataset 1 - Crime Data**

Dataset: **FBI Uniform Crime Reporting (UCR)**

Source:  
[https://crime-data-explorer.fr.cloud.gov](https://crime-data-explorer.fr.cloud.gov/)

Data Includes:

- Violent crime rates
- Property crime
- County/state identifiers
- Year

Variables:

- county
- state
- year
- violent_crime_rate
- property_crime_rate

Why it's good:

- Official federal dataset
- Widely used for research
- Easy to analyze

Crime statistics like these are collected nationally to track patterns in violent and property crime across jurisdictions. ([GitHub](https://github.com/codeforamerica/open-civic-datasets?utm_source=chatgpt.com))

# **Dataset 2 - Economic Data**

Dataset: **Bureau of Labor Statistics (BLS) Local Area Unemployment Statistics**

Source:  
<https://www.bls.gov/lau/>

Variables:

- unemployment rate
- labor force
- employment
- county
- year

The **Bureau of Labor Statistics publishes employment and wage datasets covering counties and states**, making them useful for regional economic analysis. ([Bureau of Labor Statistics](https://www.bls.gov/rda/what-datasets-are-available.htm?utm_source=chatgpt.com))

Why it's good:

- Government source
- Same geographic identifiers
- Economic variables

# **Dataset 3 (Optional but makes project stronger)**

Dataset: **U.S. Census American Community Survey (ACS)**

Source:  
[https://data.census.gov](https://data.census.gov/)

Variables:

- median household income
- population
- poverty rate
- education levels
- county FIPS code

The U.S. Census provides large public datasets on population, income, and demographics that are commonly used in data analysis projects. ([Census.gov](https://www.census.gov/data/datasets/2013/econ/susb.html?utm_source=chatgpt.com))

# **How the Datasets Connect**

All three datasets share:

**County FIPS Code**

Example merge key:

county_fips

year

Final merged dataset example:

| **county** | **year** | **crime_rate** | **unemployment_rate** | **median_income** | **population** |
| --- | --- | --- | --- | --- | --- |

# **Analysis You Can Do**

This is where you get easy points.

### **1\. Data Cleaning**

- Standardize county identifiers
- Handle missing values
- Convert datasets to same year range

### **2\. Data Integration**

Merge datasets using:

county_fips

year



### **3\. Exploratory Data Analysis**

Examples:

**Correlation**

- crime rate vs unemployment
- crime rate vs income

**Visualizations**

- scatter plot: unemployment vs crime
- heatmap of crime by state
- time trend analysis

### **4\. Regression Analysis**

Example model:

crime_rate =

β0 + β1(unemployment_rate)

\+ β2(median_income)

\+ β3(population)

\+ ε

Goal:

- Identify strongest predictors of crime.

# **Why Professors Like This Project**

It demonstrates:

✔ **Data integration  
**✔ **Multiple datasets  
**✔ **Real-world data sources  
**✔ **Statistical analysis  
**✔ **Policy/business insights**

# **Alternative (Even Easier Topic)**

If crime data feels messy, do this instead:

## **Housing Prices vs Income**

Datasets:

- **Zillow housing prices**
- **Census median income**
- **Population data**

Question:

Do areas with higher income experience faster housing price growth?

#

# **Project Plan**

## **Overview**

Our goal for this project is to analyze the relationship between economic conditions and crime rates across the United States. Specifically, we want to examine whether higher unemployment rates are associated with higher levels of crime at the county level. Understanding this relationship is important because economic conditions can influence outcomes, and identifying these patterns could potentially help policymakers, businesses, or even communities make better decisions.

Our approach will involve using two datasets, one is crime statistics from the FBI's Uniform Crime Reporting system and the other is unemployment data from the Bureau of Labor Statistics. Each dataset has different but complementary information about counties across the United States. The FBI dataset includes measures of crime rates, such as violent crime and property crime, while the BLS dataset has economic indicators such as unemployment rates and labor force participation.

To do this analysis, we will first collect and review the datasets to ensure that they contain compatible identifiers such as county names, state identifiers, and year variables. After acquiring the data, we will perform data cleaning to address missing values, inconsistent formatting, and other potential data quality issues. This step is necessary because real-world datasets often contain inconsistencies that must be fixed before we can do real analysis.

Once the datasets are cleaned, we will integrate them by merging the crime data with unemployment data using shared identifiers such as county and year. This integrated dataset will allow us to examine how unemployment levels correspond to crime rates across different regions and time periods.

After integrating the data, we will perform exploratory data analysis and statistical analysis to identify trends, correlations, and potential relationships between unemployment and crime. We will probably use visualizations such as scatter plots, trend lines, and geographic comparisons to help us show any patterns found in the data.

Ultimately, this project will hopefully demonstrate how combining multiple datasets can produce deeper insights into complex social and economic relationships.

# **Team**

### **Arjun - Data Acquisition, Integration, and Visualization**

Responsibilities:

- Download relevant datasets from reliable public sources
- Merge crime and unemployment datasets using shared identifiers
- Create charts and graphs illustrate key patterns and relationships within integrated dataset
- Collaborate with Kishan to perform statistical analysis, including correlation and regression tests, to evaluate relationship between unemployment and crime rates

### **Kishan - Data Cleaning and Exploratory Analysis**

Responsibilities:

- Standardize data formats, address missing values, ensure identifiers are consistent across datasets
- Conduct exploratory analysis on integrated dataset to identify trends and potential relationships between variables
- Collaborate with Arjun to perform statistical analysis, including correlation and potentially regression tests, to evaluate the relationship between unemployment and crime rates

We are both going to collaborate on reviewing results, writing the documentation, and finalizing the project report.

# **Research / Business Questions**

The primary goal of our project is to understand how economic conditions may influence crime patterns.

### Primary Research Question: **Is there a relationship between unemployment rates and crime rates across U.S. counties?**

### Some other research questions we aim to answer

- Do counties with higher unemployment rates tend to experience higher levels of violent crime?
- Is there a measurable correlation between unemployment rates and property crime rates?
- Are there patterns in how unemployment and crime interact across different regions of the United States?

# **Datasets**

We will use two datasets that provide complementary information and can be integrated using shared identifiers, such as county and year.

## **Dataset 1: FBI Uniform Crime Reporting (UCR)**

Source: FBI Crime Data Explorer  
<https://crime-data-explorer.fr.cloud.gov>

The FBI Uniform Crime Reporting (UCR) dataset has official crime statistics reported by law enforcement agencies across the United States. This dataset includes detailed information about different categories of crime and is widely used by researchers, policymakers, and public safety organizations.

Key variables:

- County or jurisdiction name
- State identifier
- Year
- Violent crime rate
- Property crime rate
- Total crime incidents

This dataset provides the primary outcome variables for the analysis. By examining violent and property crime rates, we can measure crime levels across counties and compare them with economic indicators from the unemployment dataset.

## **Dataset 2: Bureau of Labor Statistics Local Area Unemployment Statistics (LAUS)**

Source: Bureau of Labor Statistics  
<https://www.bls.gov/lau/>

The Local Area Unemployment Statistics (LAUS) dataset from the Bureau of Labor Statistics has monthly and annual employment data for counties and states throughout the United States. The dataset measures labor market conditions and is widely used for economic research and policy analysis.

Key variables:

- County identifier
- State identifier
- Year
- Unemployment rate
- Labor force size
- Employment levels

This dataset has economic indicators that may influence crime patterns. The unemployment rate will serve as the primary explanatory variable used to evaluate whether economic stress is associated with higher crime rates.

## **Dataset Integration**

The two datasets have several attributes that make them able to be integrated.

- County name or county FIPS code
- State identifier
- Year

By merging the datasets using these identifiers, we will create a unified dataset with both crime statistics and unemployment data for each county and year. This integrated dataset will allow us to perform meaningful comparisons and statistical analysis.

# **Timeline**

The following timeline outlines the main tasks required to complete the project and assigns responsibility for each task.

| **Task** | **Description** | **Responsible Member** | **Target Completion** |
| --- | --- | --- | --- |
| Data Acquisition | Download datasets and upload them to GitHub | Arjun | Week 2 |
| --- | --- | --- | --- |
| Data Cleaning | Standardize formats and address missing values | Kishan | Week 3 |
| --- | --- | --- | --- |
| Data Integration | Merge crime and unemployment datasets | Arjun | Week 3 |
| --- | --- | --- | --- |
| Exploratory Data Analysis | Identify trends and correlations in the data | Kishan | Week 4 |
| --- | --- | --- | --- |
| Visualization | Create charts and graphs illustrating key patterns | Arjun | Week 4 |
| --- | --- | --- | --- |
| Statistical Analysis | Perform correlation or regression analysis | Arjun and Kishan | Week 5 |
| --- | --- | --- | --- |
| Documentation | Write final report and update project documentation | Arjun and Kishan | Week 5 |
| --- | --- | --- | --- |

# **Constraints**

Data completeness, so not all counties may report crime data consistently across all years, and so missing data could reduce the number of observations available for analysis.

Reporting differences, as crime data is collected from local law enforcement agencies, they may use different reporting practices, which could create some inconsistencies in our data.

County names or identifiers may not perfectly match across the two datasets, so this might affect our ability to integration the data. We might have to do additional cleaning and transformation.

# **Gaps**

First, we need to confirm that both datasets contain consistent county identifiers that allow accurate merging. If inconsistencies are there, we might have to do some additional preprocessing.

Second, further exploration of the datasets may show additional variables that could improve the analysis.

We may alter our analytical methods as we further explore the data. While the current plan includes correlation and visualization analysis, we may also consider regression modeling or geographic comparisons if the data supports it.
