key = input("Enter key: ")
if len(key) == 10:
    print("Valid Password")
    n = int(input("Enter number: "))
    readings = []
    for i in range(n):
        x = int(input())
        readings.append(x)
    efficient = []
    moderate = []
    high = []
    invalid = []
    
    for i in range(n):
        val = readings[i]
        if val < 0:
            invalid.append(val)
        elif val <= 50:
            efficient.append(val)
        elif val <= 150:
            moderate.append(val)
        else:
            high.append(val)

    total = 0
    for i in range(n):
        if readings[i] >= 0:
            total = total + readings[i]
    if len(high) > 3:
        result = "Over use"
    elif total > 600:
        result = "Waste"
    elif len(efficient) - len(moderate) <= 1 and len(moderate) - len(efficient) <= 1:
        result = "Good"
    else:
        result = "Normal"

    print("Efficient:", efficient)
    print("Moderate:", moderate)
    print("High:", high)
    print("Invalid:", invalid)

    print("Total:", total)
    print("Count:", n)
    print("Result:", result)

else:
    print("Wrong key")
