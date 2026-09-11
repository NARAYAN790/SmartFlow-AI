import pandas as pd
from pathlib import Path

# --------------------------------------------------
# SMARTFLOW AI - DATA PROCESSING
# --------------------------------------------------

# File paths
input_file = Path("data") / "water_sensor_data.csv"
output_file = Path("data") / "processed_water_data.csv"

# Load dataset
df = pd.read_csv(input_file)

print("=" * 60)
print("       SMARTFLOW AI - DATA PROCESSING")
print("=" * 60)

print("\n1. Original Dataset")
print(f"Rows    : {len(df)}")
print(f"Columns : {len(df.columns)}")

# --------------------------------------------------
# STEP 1: Convert timestamp
# --------------------------------------------------

df["timestamp"] = pd.to_datetime(df["timestamp"])

# --------------------------------------------------
# STEP 2: Check missing values
# --------------------------------------------------

print("\n2. Missing Values")
print(df.isnull().sum())

# Remove rows with missing values if any
df = df.dropna().reset_index(drop=True)

# --------------------------------------------------
# STEP 3: Remove duplicate records
# --------------------------------------------------

duplicates = df.duplicated().sum()

print(f"\n3. Duplicate Records: {duplicates}")

df = df.drop_duplicates().reset_index(drop=True)

# --------------------------------------------------
# STEP 4: Validate numeric values
# --------------------------------------------------

# Flow rate cannot be negative
df = df[df["flow_rate_lpm"] > 0]

# Duration cannot be negative or zero
df = df[df["duration_min"] > 0]

# Consumption cannot be negative
df = df[df["consumption_liters"] > 0]

# --------------------------------------------------
# STEP 5: Feature Engineering
# --------------------------------------------------

# Time-based features
df["hour"] = df["timestamp"].dt.hour

df["day_of_week"] = df["timestamp"].dt.dayofweek

# Weekend indicator
df["is_weekend"] = (
    df["day_of_week"] >= 5
).astype(int)

# Recalculate consumption for consistency
df["calculated_consumption"] = (
    df["flow_rate_lpm"] *
    df["duration_min"]
)

# Difference between stored and calculated consumption
df["consumption_difference"] = (
    df["consumption_liters"] -
    df["calculated_consumption"]
).abs()

# --------------------------------------------------
# STEP 6: Encode zones
# --------------------------------------------------

# Numerical zone identifier
df["zone_id"] = (
    df["zone"].astype("category").cat.codes
)

# --------------------------------------------------
# STEP 7: Select ML features
# --------------------------------------------------

ml_features = [
    "flow_rate_lpm",
    "consumption_liters",
    "duration_min",
    "hour",
    "day_of_week",
    "is_weekend"
]

# --------------------------------------------------
# STEP 8: Save processed dataset
# --------------------------------------------------

df.to_csv(
    output_file,
    index=False
)

# --------------------------------------------------
# FINAL REPORT
# --------------------------------------------------

print("\n4. Feature Engineering Completed")

print("\nML Features:")
for feature in ml_features:
    print(" -", feature)

print("\n5. Processed Dataset")
print(f"Rows    : {len(df)}")
print(f"Columns : {len(df.columns)}")

print("\n6. Scenario Distribution")
print(df["scenario"].value_counts())

print("\n7. Sample Processed Records")
print(
    df[
        [
            "timestamp",
            "zone",
            "flow_rate_lpm",
            "consumption_liters",
            "duration_min",
            "hour",
            "day_of_week",
            "is_weekend",
            "scenario"
        ]
    ].head().to_string(index=False)
)

print("\n" + "=" * 60)
print("PROCESSING COMPLETED SUCCESSFULLY!")
print("=" * 60)

print(f"\nProcessed file saved at:")
print(output_file.resolve())