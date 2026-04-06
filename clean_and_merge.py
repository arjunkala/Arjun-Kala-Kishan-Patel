#!/usr/bin/env python3


import pandas as pd
import re

crime_raw = pd.read_csv("data/raw/state_crime.csv")
unemp_raw = pd.read_csv("data/raw/Unemployment2023.csv")

print(f"Crime raw shape: {crime_raw.shape}")
print(f"Unemployment raw shape: {unemp_raw.shape}")

crime = crime_raw.rename(columns={
    "Data.Population":              "population",
    "Data.Rates.Property.All":      "property_crime_rate",
    "Data.Rates.Property.Burglary": "burglary_rate",
    "Data.Rates.Property.Larceny":  "larceny_rate",
    "Data.Rates.Property.Motor":    "motor_theft_rate",
    "Data.Rates.Violent.All":       "violent_crime_rate",
    "Data.Rates.Violent.Assault":   "assault_rate",
    "Data.Rates.Violent.Murder":    "murder_rate",
    "Data.Rates.Violent.Rape":      "rape_rate",
    "Data.Rates.Violent.Robbery":   "robbery_rate",
    "Data.Totals.Property.All":     "property_crime_total",
    "Data.Totals.Property.Burglary":"burglary_total",
    "Data.Totals.Property.Larceny": "larceny_total",
    "Data.Totals.Property.Motor":   "motor_theft_total",
    "Data.Totals.Violent.All":      "violent_crime_total",
    "Data.Totals.Violent.Assault":  "assault_total",
    "Data.Totals.Violent.Murder":   "murder_total",
    "Data.Totals.Violent.Rape":     "rape_total",
    "Data.Totals.Violent.Robbery":  "robbery_total",
})

crime = crime[crime["State"] != "United States"]

crime = crime[(crime["Year"] >= 2000) & (crime["Year"] <= 2019)].copy()

print(f"Crime after cleaning: {crime.shape} | Missing: {crime.isnull().sum().sum()}")

state_unemp = unemp_raw[
    (unemp_raw["FIPS_Code"] % 1000 == 0) &
    (unemp_raw["FIPS_Code"] != 0)
].copy()

def extract_year(attr):
    m = re.search(r"(\d{4})", attr)
    return int(m.group(1)) if m else None

def extract_metric(attr):
    return re.sub(r"_\d{4}$", "", attr)

state_unemp["Year"]   = state_unemp["Attribute"].apply(extract_year)
state_unemp["Metric"] = state_unemp["Attribute"].apply(extract_metric)

unemp_wide = state_unemp.pivot_table(
    index=["Area_Name", "State", "Year"],
    columns="Metric",
    values="Value",
    aggfunc="first"
).reset_index()
unemp_wide.columns.name = None

unemp_wide = unemp_wide[(unemp_wide["Year"] >= 2000) & (unemp_wide["Year"] <= 2019)].copy()

state_abbrev = {
    "AL":"Alabama","AK":"Alaska","AZ":"Arizona","AR":"Arkansas","CA":"California",
    "CO":"Colorado","CT":"Connecticut","DE":"Delaware","FL":"Florida","GA":"Georgia",
    "HI":"Hawaii","ID":"Idaho","IL":"Illinois","IN":"Indiana","IA":"Iowa",
    "KS":"Kansas","KY":"Kentucky","LA":"Louisiana","ME":"Maine","MD":"Maryland",
    "MA":"Massachusetts","MI":"Michigan","MN":"Minnesota","MS":"Mississippi","MO":"Missouri",
    "MT":"Montana","NE":"Nebraska","NV":"Nevada","NH":"New Hampshire","NJ":"New Jersey",
    "NM":"New Mexico","NY":"New York","NC":"North Carolina","ND":"North Dakota","OH":"Ohio",
    "OK":"Oklahoma","OR":"Oregon","PA":"Pennsylvania","RI":"Rhode Island","SC":"South Carolina",
    "SD":"South Dakota","TN":"Tennessee","TX":"Texas","UT":"Utah","VT":"Vermont",
    "VA":"Virginia","WA":"Washington","WV":"West Virginia","WI":"Wisconsin","WY":"Wyoming",
    "DC":"District of Columbia"
}
unemp_wide["State"] = unemp_wide["State"].map(state_abbrev)

print(f"Unemployment after cleaning: {unemp_wide.shape} | Missing: {unemp_wide.isnull().sum().sum()}")

unemp_select = unemp_wide[[
    "State", "Year",
    "Unemployment_rate",
    "Civilian_labor_force",
    "Employed",
    "Unemployed",
    "Median_Household_Income"
]]

merged = pd.merge(crime, unemp_select, on=["State", "Year"], how="inner")

print(f"Merged dataset shape: {merged.shape}")
print(f"States matched: {merged['State'].nunique()}")
print(f"Years covered: {merged['Year'].min()} - {merged['Year'].max()}")
print(f"Total missing values: {merged.isnull().sum().sum()}")

crime.to_csv("data/processed/crime_clean.csv", index=False)
unemp_wide.to_csv("data/processed/unemployment_clean.csv", index=False)
merged.to_csv("data/processed/merged_crime_unemployment.csv", index=False)

print("\n✓ Saved: data/processed/crime_clean.csv")
print("✓ Saved: data/processed/unemployment_clean.csv")
print("✓ Saved: data/processed/merged_crime_unemployment.csv")
print("\n=== FINAL MERGED SAMPLE ===")
print(merged[["State","Year","violent_crime_rate","property_crime_rate","Unemployment_rate","Median_Household_Income"]].head(10).to_string())
