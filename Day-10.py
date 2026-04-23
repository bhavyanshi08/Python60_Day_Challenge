import random
import copy
import pandas as pd
import numpy as np
import math

roll_number = int(input("Enter your roll number: "))

def generate_zone_data():
    data = []

    for i in range(1, 16):
        record = {
            "zone": i,
            "metrics": {
                "traffic": random.randint(20, 100),
                "pollution": random.randint(30, 300),
                "energy": random.randint(50, 500)
            },
            "history": [random.randint(10, 100) for _ in range(3)]
        }
        data.append(record)

    return data


def personalize_dataset(data):
    if roll_number % 2 == 0:
        data.reverse()
        print("\nEven Roll Number Rule Applied: Dataset Reversed\n")
    else:
        data = data[3:] + data[:3]
        print("\nOdd Roll Number Rule Applied: Dataset Rotated by 3\n")

    return data


def create_copies(data):
    assignment_copy = data
    shallow_copy = copy.copy(data)
    deep_copy = copy.deepcopy(data)

    return assignment_copy, shallow_copy, deep_copy


def mutate_data(shallow_copy):
    shallow_copy[0]["metrics"]["traffic"] += 50
    shallow_copy[0]["metrics"]["pollution"] += 40
    shallow_copy[0]["metrics"]["energy"] += 60

    shallow_copy[0]["history"].append(999)

    total = (
        shallow_copy[0]["metrics"]["traffic"] +
        shallow_copy[0]["metrics"]["pollution"] +
        shallow_copy[0]["metrics"]["energy"]
    )

    shallow_copy[0]["risk_score"] = math.log(total)

    return shallow_copy


def convert_to_dataframe(data):
    rows = []

    for item in data:
        rows.append({
            "zone": item["zone"],
            "traffic": item["metrics"]["traffic"],
            "pollution": item["metrics"]["pollution"],
            "energy": item["metrics"]["energy"]
        })

    df = pd.DataFrame(rows)
    return df


def custom_risk_score(df):
    df["risk"] = np.log(
        df["traffic"] * 0.4 +
        df["pollution"] * 0.4 +
        df["energy"] * 0.2
    )

    return df


def analyze_data(df):
    print("\nMean Values:")
    print(df[["traffic", "pollution", "energy"]].mean())

    print("\nVariance:")
    print(df[["traffic", "pollution", "energy"]].var())

    traffic = df["traffic"].values
    pollution = df["pollution"].values

    correlation = np.sum(
        (traffic - np.mean(traffic)) *
        (pollution - np.mean(pollution))
    ) / (
        np.sqrt(np.sum((traffic - np.mean(traffic))**2)) *
        np.sqrt(np.sum((pollution - np.mean(pollution))**2))
    )

    print("\nManual Correlation (Traffic vs Pollution):")
    print(correlation)

    threshold = df["risk"].mean() + df["risk"].std()
    anomalies = df[df["risk"] > threshold]

    print("\nAnomaly Zones:")
    print(anomalies[["zone", "risk"]])

    return anomalies


def detect_patterns(original, shallow_copy, df):
    print("\nBEFORE vs AFTER Comparison")

    print("\nOriginal Data:")
    print(original[0])

    print("\nShallow Copy:")
    print(shallow_copy[0])

    if original[0] == shallow_copy[0]:
        print("\nHidden Corruption Detected: Original affected due to shallow copy")

    risky_zones = df[df["risk"] > df["risk"].mean()]

    print("\nHigh Risk Zones:")
    print(risky_zones["zone"].tolist())

    print("\nCluster Detection:")
    zones = risky_zones["zone"].tolist()

    for i in range(len(zones)-1):
        if zones[i+1] - zones[i] == 1:
            print(f"Cluster found between Zone {zones[i]} and Zone {zones[i+1]}")


def final_decision(df):
    max_risk = df["risk"].max()
    min_risk = df["risk"].min()

    stability_index = 1 / (df["risk"].var())

    result_tuple = (max_risk, min_risk, stability_index)

    print("\nRisk Tuple:")
    print(result_tuple)

    avg_risk = df["risk"].mean()

    if avg_risk < 4:
        print("\nFinal Decision: System Stable")
    elif avg_risk < 5:
        print("\nFinal Decision: Moderate Risk")
    elif avg_risk < 6:
        print("\nFinal Decision: High Corruption Risk")
    else:
        print("\nFinal Decision: Critical Failure")

    return result_tuple


data = generate_zone_data()

print("BEFORE Mutation:")
print(data)

data = personalize_dataset(data)

assignment_copy, shallow_copy, deep_copy = create_copies(data)

mutate_data(shallow_copy)

print("\nAFTER Mutation:")
print(data)

df = convert_to_dataframe(data)

df = custom_risk_score(df)

print("\nDataFrame:")
print(df)

analyze_data(df)

detect_patterns(data, shallow_copy, df)

print("\nDeep Copy Safe Data:")
print(deep_copy[0])

print("\nWhy shallow copy corrupts nested structures?")
print("Because it copies only outer objects while inner dictionaries and lists still share references.")

final_decision(df)
