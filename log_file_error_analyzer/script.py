error_counts = {}

# take file path from user
log_file = input("Enter log file path: ")

with open(log_file, "r") as file:
    for line in file:
        if "error" in line.lower() or "critical" in line.lower():
            error = line.strip()
            error_counts[error] = error_counts.get(error, 0) + 1

print("\nSummary Report:\n")

for error, count in error_counts.items():
    print(f"{error} : {count}")
