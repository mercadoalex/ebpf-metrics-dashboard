import threading
import time

# Flag to control the activity loop
activity_running = False

def generate_activity():
    global activity_running
    print("Starting activity generation...")
    activity_running = True
    count = 0

    # Simulate CPU-intensive activity in a loop
    while activity_running:
        for _ in range(10**6):
            count += 1
        print(f"Activity count: {count}")
        time.sleep(1)  # Simulate periodic activity

    print("Activity generation stopped.")

def stop_activity():
    global activity_running
    activity_running = False