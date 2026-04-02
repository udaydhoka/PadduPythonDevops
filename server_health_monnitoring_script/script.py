import psutil


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

    if memory > 80:
        print("⚠️ Memory is high!")

    if disk > 80:
        print("⚠️ Disk is high!")

    