import psutil
import sys


while True:
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    print("\nChecking system...")

    print("CPU:", cpu)
    print("Memory:", memory)
    print("Disk:", disk)

    if cpu > 80:
        print("⚠️ CPU is high!")
        sys.exit()

    if memory > 80:
        print("⚠️ Memory is high!")
        sys.exit()

    if disk > 80:
        print("⚠️ Disk is high!")
        sys.exit()