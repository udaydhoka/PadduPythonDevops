log_counts = {}

# take file path from user
log_file = input("Enter log file path: ")

# take log type input
log_type = input("Enter log type to search (error/warning/info): ").lower()

try:
    with open(log_file, "r") as file:
        for line in file:
            if log_type in line.lower():
                log = line.strip()
                log_counts[log] = log_counts.get(log, 0) + 1

    print(f"\nSummary Report for '{log_type.upper()}' logs:\n")

    if log_counts:
        for log, count in log_counts.items():
            print(f"{log} : {count}")
    else:
        print(f"No '{log_type}' logs found.")

except FileNotFoundError:
    print("Error: File not found. Please check the file path.")
except Exception as e:
    print(f"Unexpected error occurred: {e}")