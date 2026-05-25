# Update: Conversion of the legacy kyoto wdc geomagnetic storm compressed text data into clean individual
# Regex Parsed DST values

import re

file_path = "../data/dst_raw.csv"

with open(file_path, "r") as file:
    lines = file.readlines()

line = lines[0].split()

# Remove metadata
data_values = line[2:]

clean_values = []

for item in data_values:

    # Extract groups like 000 or -006
    values = re.findall(r'-?\d{3}', item)

    clean_values.extend(values)

print(clean_values[:30])

# Building an actual DST time-series dataframe
# Convert values into Integers
# Create hourly timestamps
# Build a pandas dataframe
# Generate my first DST Storm plot

import re
import pandas as pd

file_path = "../data/dst_raw.csv"

with open(file_path, "r") as file:
    lines = file.readlines()

all_values = []

for line in lines:

    parts = line.split()

    # Remove metadata
    data_values = parts[2:]

    for item in data_values:

        # Extract values like 000 or -006
        values = re.findall(r'-?\d{3}', item)

        all_values.extend(values)

# Convert strings to integers
dst_values = [int(value) for value in all_values]

 # Scientific Preprocessing
 # My DST Dataset is now officially converted into a clean numerical dataframe
 # Built the core analytical asset for the geomagnetic storm project:
 # Raw Kyoto WDC archive ---> Regex Parsing ----> Numerical Extraction ---> Pandas dataframe

 # Create a Time Series
 # We have only: 0, -6, -2...But Geomagnetic analysis requires: DateTime + DST_Value
 # Create an hourly timestamp index that covers Jan-April 2000 an DST values are hourly
 # 24 hours per day, a continous hourly sequence

import re
import pandas as pd

file_path = "../data/dst_raw.csv"

with open(file_path, "r") as file:
    lines = file.readlines()

all_values = []

for line in lines:

    parts = line.split()

    # Remove metadata
    data_values = parts[2:]

    for item in data_values:

        values = re.findall(r'-?\d{3}', item)

        all_values.extend(values)

# Convert to integers
dst_values = [int(value) for value in all_values]

# Create hourly timestamps
dates = pd.date_range(
    start='2000-01-01',
    periods=len(dst_values),
    freq='h'
)
# Create dataframe: # Addition of Time Series (Jan- Apr)
# Keep only Jan-Apr 2000 period
df = pd.DataFrame({
    'DateTime': dates,
    'DST_Value': dst_values
})

df = df.iloc[:2904]
print(df.shape)

# Display first rows
print(df.head())

# Display dataframe information
print(df.info())

#Storm classification function
def classify_storm(dst):
    def classify_storm(dst):

        if dst <= -200:
            return "Extreme Storm"

        elif dst <= -100:
            return "Severe Storm"

        elif dst <= -50:
            return "Moderate Storm"

        elif dst < -20:
            return "Weak Disturbance"

        else:
            return "Quiet"

# Create DST Plot
import re
import pandas as pd
import matplotlib.pyplot as plt

file_path = "../data/dst_raw.csv"

with open(file_path, "r") as file:
    lines = file.readlines()

all_values = []

for line in lines:

    parts = line.split()

    # Remove metadata
    data_values = parts[2:]

    for item in data_values:

        values = re.findall(r'-?\d{3}', item)

        all_values.extend(values)

# Convert values to integers
dst_values = [int(value) for value in all_values]

# Create hourly timestamps
dates = pd.date_range(
    start='2000-01-01',
    periods=len(dst_values),
    freq='h'
)
# Create dataframe
df = pd.DataFrame({
    'DateTime': dates,
    'DST_Value': dst_values
})
# Storm classification function
def classify_storm(dst):

    if dst < -100:
        return "Intense Storm"

    elif dst < -50:
        return "Moderate Storm"

    else:
        return "Quiet"

# Apply classification
df['Storm_Class'] = df['DST_Value'].apply(classify_storm)

# Display first rows
print(df.head())

# Storm class counts
print(df['Storm_Class'].value_counts())


# Clean Verification step
print(df['Storm_Class'].value_counts())

print(df[['DateTime', 'DST_Value', 'Storm_Class']].head(20))

print(df[df['Storm_Class'] != "Quiet"].head(20))

 # Diagnostic Check
print(df['DST_Value'].describe())
# Second Check
print(df['DST_Value'].head(20))
print(df['DST_Value'].tail(20))

 # Improved Storm Classification
# Storm classification function
def classify_storm(dst):

    if dst <= -200:
        return "Extreme Storm"

    elif dst <= -100:
        return "Severe Storm"

    elif dst <= -50:
        return "Moderate Storm"

    elif dst < -20:
        return "Weak Disturbance"

    else:
        return "Quiet"

    # Apply classification
    df['Storm_Class'] = df['DST_Value'].apply(classify_storm)
    # Show results
    print(df['Storm_Class'].value_counts())

    # Optional preview
    print(df.head(10))

# Plotting section
plt.figure(figsize=(14,6))

# Quiet / weak conditions
quiet = df[df['DST_Value'] > -50]

plt.plot(
    quiet['DateTime'],
    quiet['DST_Value'],
    color='blue',
    linewidth=0.7,
    label='Quiet / Weak'
)

# Moderate storms
moderate = df[
    (df['DST_Value'] <= -50) &
    (df['DST_Value'] > -100)
]

plt.scatter(
    moderate['DateTime'],
    moderate['DST_Value'],
    color='orange',
    s=8,
    label='Moderate Storm'
)

# Severe storms
severe = df[
    (df['DST_Value'] <= -100) &
    (df['DST_Value'] > -200)
]

plt.scatter(
    severe['DateTime'],
    severe['DST_Value'],
    color='red',
    s=10,
    label='Severe Storm'
)

# Extreme storms
extreme = df[df['DST_Value'] <= -200]

plt.scatter(
    extreme['DateTime'],
    extreme['DST_Value'],
    color='darkred',
    s=15,
    label='Extreme Storm'
)

# Threshold lines
plt.axhline(-50, linestyle='--')
plt.axhline(-100, linestyle='--')
plt.axhline(-200, linestyle='--')

plt.title('Kyoto DST Geomagnetic Storm Analysis')
plt.xlabel('Date')
plt.ylabel('DST Index (nT)')

plt.legend()
plt.grid(True)

plt.tight_layout()

plt.show()
