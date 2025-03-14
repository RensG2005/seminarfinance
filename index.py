import numpy as np
import pandas as pd

aexcsv = pd.read_csv("data_aex.csv", sep=';')

aexcsv['Date'] = pd.to_datetime(aexcsv['Date'])

print(aexcsv["Date"])

# Filter for VTI and TLT ETFs
aexcsv = aexcsv[aexcsv['ticker'].isin(['VTI', 'TLT'])]  

# Sort data by Date and Ticker
aexcsv = aexcsv.sort_values(by=['ticker', 'Date'])

# Compute daily returns
aexcsv['Return'] = aexcsv.groupby('ticker')['Adj Close'].pct_change()

# Save to CSV
aexcsv.to_csv("returns_data.csv", index=False)

# Display results
print(aexcsv.head())
