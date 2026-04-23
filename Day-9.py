import copy

roll_number = int(input("Enter your roll number: "))
def build_server_records():
    users = [
        {
            "id": 1,
            "data": {
                "files": ["a.txt", "b.txt"],
                "usage": 500
            }
        },
        {
            "id": 2,
            "data": {
                "files": ["c.txt"],
                "usage": 300
            }
        }
    ]
    return users

def create_replica_versions(users):
    assigned_data = users
    shallow_data = copy.copy(users)
    deep_data = copy.deepcopy(users)
    return assigned_data, shallow_data, deep_data

def trigger_mutation(replica):
    if roll_number % 2 == 0:
        replica[0]["data"]["files"].append("backup_file.txt")
        print("Even Roll Number Rule Applied: New file added\n")
    else:
        if replica[0]["data"]["files"]:
            replica[0]["data"]["files"].pop()
        print("Odd Roll Number Rule Applied: File removed\n")
    replica[0]["data"]["usage"] = 900
    if len(replica[1]["data"]["files"]) > 0:
        replica[1]["data"]["files"].pop()
    return replica

def audit_integrity(original, shallow_data, deep_data):
    leakage_count = 0
    safe_count = 0

    if original == shallow_data:
        leakage_count += 1
    if original != deep_data:
        safe_count += 1
    original_files = set()
    modified_files = set()

    for user in original:
        for file in user["data"]["files"]:
            original_files.add(file)

    for user in shallow_data:
        for file in user["data"]["files"]:
            modified_files.add(file)
    overlap = original_files.intersection(modified_files)
    overlap_count = len(overlap)
    print("\nIntegrity Report:")

    if leakage_count > 0:
        print("Data Leakage Detected")
    if safe_count > 0:
        print("Deep Copy Safe")

    print("Common Files:", overlap)

    print("\nWhy inner list got affected?")
    print("Shallow copy copies only outer structure, inner nested lists share same reference.")
    return (leakage_count, safe_count, overlap_count)

original_data = build_server_records()
print("\nBEFORE Modification:")
print(original_data)
assigned_data, shallow_data, deep_data = create_replica_versions(original_data)
trigger_mutation(shallow_data)

print("\nAFTER Modification:")

print("\nOriginal Data:")
print(original_data)

print("\nAssignment Copy:")
print(assigned_data)

print("\nShallow Copy:")
print(shallow_data)

print("\nDeep Copy:")
print(deep_data)

result = audit_integrity(original_data, shallow_data, deep_data)
print("\nIntegrity Tuple:")
print(result)

print("\nCustom Data Corruption Rule:")
print("Data corruption occurs when copied data unintentionally alters original records.")