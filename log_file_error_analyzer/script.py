error_counts = {}

with open("E:\\PadduPythonDevops\\log_file_error_analyzer\\app.log", "r") as file:
    for line in file:
        if "ERROR" in line or "CRITICAL" in line:
            error = line.strip()

            if error in error_counts:
                error_counts[error] += 1
            else:
                error_counts[error] = 1

print("Summary Report:\n")

for error, count in error_counts.items():
    print(f"{error} : {count}")