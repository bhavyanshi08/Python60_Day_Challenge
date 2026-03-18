a=input("enter the Password:")
if len(a) == 6 and a == "ganesh":
    print("Valid password")
    n=int(input("Enter the no of readings: "))
    readings= [0] * n
    for i in range(n):
        readings[i] = int(input())
    usage = {
        "efficient": [],
        "moderate": [],
        "high": [],
        "invalid": []
    }
    for e in readings:
        if e < 0:
            usage["invalid"].append(e)
        elif 0 <= e <= 50:
            usage["efficient"].append(e)
        elif 51 <= e <= 150:
            usage["moderate"].append(e)
        else:
            usage["high"].append(e)
    valid_readings = [x for x in readings if x >= 0]
    total_consumption = sum(valid_readings)
    num_buildings = len(readings)
    if len(usage["high"]) > 3:
        result = "Overconsumption Detected"
    elif total_consumption > 600:
        result = "Energy Waste Detected"
    elif abs(len(usage["efficient"]) - len(usage["moderate"])) <= 1:
        result = "Efficient Campus"
    else:
        result = "Moderate Usage"
    print("\nCategorized Readings:")
    for key, value in usage.items():
        print(key, ":", value)

    print("\nTotal Consumption:", total_consumption)
    print("Number of Buildings:", num_buildings)
    print("\nEfficiency Result:", result)
else:
    print("Invalid Password")
