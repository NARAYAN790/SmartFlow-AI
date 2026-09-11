import pandas as pd
from pathlib import Path

# --------------------------------------------------
# SMARTFLOW AI - DECISION & EXPLANATION LAYER
# --------------------------------------------------

input_file = Path("data") / "anomaly_results.csv"
output_file = Path("data") / "decision_results.csv"

# Load model results
df = pd.read_csv(input_file)

print("=" * 65)
print("       SMARTFLOW AI - DECISION & EXPLANATION LAYER")
print("=" * 65)

# --------------------------------------------------
# DECISION LOGIC
# --------------------------------------------------

def generate_reason(row):

    if row["severity"] == "Normal":
        return "Water usage pattern is within the expected range."

    flow = row["flow_rate_lpm"]
    duration = row["duration_min"]
    consumption = row["consumption_liters"]

    if row["severity"] == "Critical":
        return (
            f"Very high flow rate ({flow:.2f} L/min) "
            f"with prolonged flow ({duration:.2f} min) "
            f"and high consumption ({consumption:.2f} L). "
            "Possible continuous leakage or major water wastage."
        )

    return (
        f"Unusual flow pattern detected: "
        f"{flow:.2f} L/min for {duration:.2f} min, "
        f"using approximately {consumption:.2f} L. "
        "Possible abnormal usage or early-stage leakage."
    )


def generate_action(row):

    if row["severity"] == "Normal":
        return "No immediate action required."

    if row["severity"] == "Critical":
        return (
            "Immediate inspection recommended. "
            "Check taps, pipes, valves and nearby water lines."
        )

    return (
        "Schedule inspection of the zone and monitor "
        "the next water-flow readings."
    )


# --------------------------------------------------
# APPLY DECISION LOGIC
# --------------------------------------------------

df["reason"] = df.apply(
    generate_reason,
    axis=1
)

df["recommended_action"] = df.apply(
    generate_action,
    axis=1
)

# --------------------------------------------------
# AGENT INPUT
# --------------------------------------------------

df["agent_input"] = (
    "Zone: " + df["zone"].astype(str)
    + " | Flow: " + df["flow_rate_lpm"].round(2).astype(str) + " L/min"
    + " | Duration: " + df["duration_min"].round(2).astype(str) + " min"
    + " | Consumption: " + df["consumption_liters"].round(2).astype(str) + " L"
    + " | Severity: " + df["severity"].astype(str)
    + " | Reason: " + df["reason"].astype(str)
)

# --------------------------------------------------
# SAVE DECISION RESULTS
# --------------------------------------------------

df.to_csv(
    output_file,
    index=False
)

# --------------------------------------------------
# SUMMARY
# --------------------------------------------------

print("\nDecision Distribution:")
print(df["severity"].value_counts())

print("\nCritical Alerts:")
print(
    (df["severity"] == "Critical").sum()
)

print("\nSuspicious Alerts:")
print(
    (df["severity"] == "Suspicious").sum()
)

print("\nSample Decision Results:")

sample = df[
    df["severity"] != "Normal"
][
    [
        "timestamp",
        "zone",
        "flow_rate_lpm",
        "duration_min",
        "consumption_liters",
        "severity",
        "reason",
        "recommended_action"
    ]
].head(5)

print(
    sample.to_string(index=False)
)

print("\n" + "=" * 65)
print("DECISION LAYER COMPLETED SUCCESSFULLY!")
print("=" * 65)

print("\nOutput file:")
print(output_file.resolve())