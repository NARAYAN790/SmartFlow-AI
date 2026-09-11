import pandas as pd
import numpy as np
from pathlib import Path

np.random.seed(42)

# Total synthetic IoT records
N = 8000

# College departments / labs
zones = [
    "CSE Department",
    "AIML Department",
    "IT Department",
    "Electronics Department",
    "BT Department",
    "Biotech Department",
    "New Seminar Hall",
    "HOD Department",
    "AI Lab",
    "Physics Lab",
    "Chemistry Lab",
    "Mechanical Lab"
]

# Generate timestamps
timestamps = pd.date_range(
    start="2026-07-01 08:00:00",
    periods=N,
    freq="10min"
)

# Randomly assign locations
zone_data = np.random.choice(zones, size=N)

# Synthetic scenarios
# This column is ONLY for validation/testing later.
scenarios = np.random.choice(
    ["Normal", "Suspicious", "Critical"],
    size=N,
    p=[0.85, 0.10, 0.05]
)

flow_rates = []
durations = []

# Prototype baseline assumptions
normal_profiles = {
    "CSE Department": (4.0, 1.0),
    "AIML Department": (4.0, 1.0),
    "IT Department": (4.2, 1.0),
    "Electronics Department": (4.5, 1.0),
    "BT Department": (4.5, 1.1),
    "Biotech Department": (5.0, 1.2),
    "New Seminar Hall": (6.0, 1.3),
    "HOD Department": (3.5, 0.8),
    "AI Lab": (5.0, 1.2),
    "Physics Lab": (5.5, 1.2),
    "Chemistry Lab": (5.5, 1.2),
    "Mechanical Lab": (6.0, 1.4)
}

# Generate synthetic sensor readings
for zone, scenario in zip(zone_data, scenarios):

    mean_flow, std_flow = normal_profiles[zone]

    if scenario == "Normal":

        flow = np.random.normal(
            mean_flow,
            std_flow
        )

        duration = np.random.uniform(1, 10)

    elif scenario == "Suspicious":

        flow = np.random.uniform(
            mean_flow * 1.8,
            mean_flow * 3.0
        )

        duration = np.random.uniform(10, 30)

    else:

        flow = np.random.uniform(
            mean_flow * 3.0,
            mean_flow * 5.0
        )

        duration = np.random.uniform(30, 90)

    flow_rates.append(max(flow, 0.5))
    durations.append(duration)

flow_rates = np.array(flow_rates)
durations = np.array(durations)

# Calculate water consumption
consumption = flow_rates * durations

# Create dataframe
df = pd.DataFrame({
    "timestamp": timestamps,
    "zone": zone_data,
    "flow_rate_lpm": np.round(flow_rates, 2),
    "consumption_liters": np.round(consumption, 2),
    "duration_min": np.round(durations, 2),
    "scenario": scenarios
})

# Shuffle records
df = df.sample(
    frac=1,
    random_state=42
).reset_index(drop=True)

# Save CSV
file_path = Path("data") / "water_sensor_data.csv"

df.to_csv(
    file_path,
    index=False
)

print()
print("=" * 55)
print("       SMARTFLOW AI - DATASET GENERATED")
print("=" * 55)
print()
print(f"Records generated : {len(df)}")
print(f"Locations         : {len(zones)}")
print(f"Output file       : {file_path.resolve()}")
print()

print("Scenario Distribution:")
print(df["scenario"].value_counts())
print()

print("Columns:")
for column in df.columns:
    print(" -", column)

print()
print("First 5 records:")
print(df.head().to_string(index=False))

print()
print("Dataset generation completed successfully!")