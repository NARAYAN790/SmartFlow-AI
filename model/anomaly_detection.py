import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.ensemble import IsolationForest

# --------------------------------------------------
# SMARTFLOW AI - ISOLATION FOREST
# --------------------------------------------------

input_file = Path("data") / "processed_water_data.csv"
output_file = Path("data") / "anomaly_results.csv"

# Load processed data
df = pd.read_csv(input_file)

print("=" * 60)
print("       SMARTFLOW AI - ANOMALY DETECTION")
print("=" * 60)

print(f"\nInput records: {len(df)}")

# --------------------------------------------------
# ML FEATURES
# --------------------------------------------------

features = [
    "flow_rate_lpm",
    "consumption_liters",
    "duration_min",
    "hour",
    "day_of_week",
    "is_weekend"
]

X = df[features]

print("\nFeatures used by Isolation Forest:")
for feature in features:
    print(" -", feature)

# --------------------------------------------------
# ISOLATION FOREST MODEL
# --------------------------------------------------

model = IsolationForest(
    n_estimators=200,
    contamination=0.10,
    random_state=42
)

# Train model
model.fit(X)

# --------------------------------------------------
# PREDICTIONS
# --------------------------------------------------

# Isolation Forest:
#  1  = Normal
# -1  = Anomaly

df["model_prediction"] = model.predict(X)

# Raw decision score
df["anomaly_score"] = model.decision_function(X)

# Convert prediction to readable status
df["ml_status"] = np.where(
    df["model_prediction"] == -1,
    "Anomaly",
    "Normal"
)

# --------------------------------------------------
# SEVERITY CLASSIFICATION
# --------------------------------------------------

# Lower anomaly score = more unusual
def classify_severity(row):

    if row["ml_status"] == "Normal":
        return "Normal"

    score = row["anomaly_score"]

    if score < -0.10:
        return "Critical"

    return "Suspicious"


df["severity"] = df.apply(
    classify_severity,
    axis=1
)

# --------------------------------------------------
# SAVE RESULTS
# --------------------------------------------------

df.to_csv(
    output_file,
    index=False
)

# --------------------------------------------------
# RESULTS
# --------------------------------------------------

print("\n" + "-" * 60)
print("MODEL RESULTS")
print("-" * 60)

print("\nML Status:")
print(df["ml_status"].value_counts())

print("\nSeverity:")
print(df["severity"].value_counts())

print("\nScenario vs Model:")
print(
    pd.crosstab(
        df["scenario"],
        df["ml_status"]
    )
)

print("\nSample Anomalies:")

anomalies = df[
    df["ml_status"] == "Anomaly"
][
    [
        "timestamp",
        "zone",
        "flow_rate_lpm",
        "consumption_liters",
        "duration_min",
        "anomaly_score",
        "severity",
        "scenario"
    ]
].head(10)

print(
    anomalies.to_string(index=False)
)

print("\n" + "=" * 60)
print("ISOLATION FOREST COMPLETED SUCCESSFULLY!")
print("=" * 60)

print(f"\nResults saved at:")
print(output_file.resolve())