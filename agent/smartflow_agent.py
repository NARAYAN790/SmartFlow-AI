import pandas as pd


def analyze_anomaly(row):
    severity = str(row["severity"]).strip().lower()
    zone = row["zone"]
    flow = float(row["flow_rate_lpm"])
    duration = float(row["duration_min"])
    consumption = float(row["consumption_liters"])
    score = float(row["anomaly_score"])

    if severity == "critical":
        explanation = (
            f"Critical water-flow anomaly detected in {zone}. "
            f"The zone recorded a flow rate of {flow:.2f} L/min "
            f"for {duration:.2f} minutes, resulting in "
            f"{consumption:.2f} liters of estimated consumption. "
            f"This pattern indicates possible continuous water flow "
            f"or suspected leakage."
        )

        recommendation = (
            "Immediate inspection is recommended. Check taps, pipes, "
            "valves, fittings, and nearby water lines."
        )

        priority = "Immediate"

    elif severity == "suspicious":
        explanation = (
            f"Suspicious water-use pattern detected in {zone}. "
            f"The recorded flow was {flow:.2f} L/min for "
            f"{duration:.2f} minutes, with estimated consumption of "
            f"{consumption:.2f} liters. "
            f"This may indicate unusual usage or early leakage."
        )

        recommendation = (
            "Schedule an inspection and continue monitoring the zone "
            "for repeated abnormal flow patterns."
        )

        priority = "Monitor / Inspect"

    else:
        explanation = (
            f"Water usage in {zone} is within the expected range. "
            f"The recorded flow was {flow:.2f} L/min for "
            f"{duration:.2f} minutes."
        )

        recommendation = "No immediate maintenance action is required."

        priority = "No Action"

    return {
        "zone": zone,
        "severity": severity.title(),
        "flow_rate_lpm": flow,
        "duration_min": duration,
        "consumption_liters": consumption,
        "anomaly_score": score,
        "explanation": explanation,
        "recommendation": recommendation,
        "priority": priority
    }


def analyze_file(file_path):
    df = pd.read_csv(file_path)

    results = []

    for _, row in df.iterrows():
        results.append(analyze_anomaly(row))

    return pd.DataFrame(results)


def summarize_anomalies(file_path):
    df = pd.read_csv(file_path)

    total = len(df)
    critical = (df["severity"].str.lower() == "critical").sum()
    suspicious = (df["severity"].str.lower() == "suspicious").sum()
    normal = (df["severity"].str.lower() == "normal").sum()

    summary = {
        "total_records": total,
        "critical": int(critical),
        "suspicious": int(suspicious),
        "normal": int(normal)
    }

    return summary


if __name__ == "__main__":

    input_file = r"data\decision_results.csv"

    print("=" * 60)
    print("SMARTFLOW AI WATER AGENT")
    print("=" * 60)

    df = pd.read_csv(input_file)

    print(f"\nTotal records analyzed: {len(df)}")

    critical_count = (df["severity"].str.lower() == "critical").sum()
    suspicious_count = (df["severity"].str.lower() == "suspicious").sum()
    normal_count = (df["severity"].str.lower() == "normal").sum()

    print(f"Critical anomalies : {critical_count}")
    print(f"Suspicious anomalies: {suspicious_count}")
    print(f"Normal records     : {normal_count}")

    print("\n" + "-" * 60)
    print("SAMPLE ANOMALY ANALYSIS")
    print("-" * 60)

    anomalies = df[df["severity"].str.lower() != "normal"]

    if len(anomalies) > 0:
        sample = anomalies.iloc[0]
        result = analyze_anomaly(sample)

        print(f"\nZone       : {result['zone']}")
        print(f"Severity   : {result['severity']}")
        print(f"Flow Rate  : {result['flow_rate_lpm']:.2f} L/min")
        print(f"Duration   : {result['duration_min']:.2f} min")
        print(f"Consumption: {result['consumption_liters']:.2f} L")
        print(f"Anomaly Score: {result['anomaly_score']:.6f}")

        print("\nAI Explanation:")
        print(result["explanation"])

        print("\nRecommended Action:")
        print(result["recommendation"])

        print(f"\nPriority: {result['priority']}")

    print("\n" + "=" * 60)
    print("Agent analysis completed successfully.")
    print("=" * 60)