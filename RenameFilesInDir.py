import os

for filename in os.listdir("."):
    if os.path.isfile(filename) and "-" in filename:
        new_filename = filename.split("-", 1)[1].strip()
        os.rename(filename, new_filename)
        print(f"{filename} → {new_filename}")

print("Done!")