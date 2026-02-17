Name = "Earla Bhavyanshi"
L = len(Name) - Name.count(" ")
PLI = L % 3
N = int(input("Enter Package weights: "))
weights = [0] * N
for i in range(0, N):
    weights[i] = int(input("weight-{i+1}: "))
very_light = []
normal_load = []
heavy_load = []
overload = []
invalid_entries = []
for i in range(N):
    if weights[i] < 0:
        invalid_entries += [weights[i]]
    elif weights[i] < 6:
        very_light += [weights[i]]
    elif weights[i] < 26:
        normal_load += [weights[i]]
    elif weights[i] < 61:
        heavy_load += [weights[i]]
    else:
        overload += [weights[i]]
valid = len(normal_load) + len(heavy_load) + len(overload)
affected = 0
if PLI == 0:
    invalid_entries += overload
    affected = len(overload)
    overload = []
