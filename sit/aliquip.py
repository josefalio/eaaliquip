import time

def timer(interval):
    start_time = time.time()
    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
        print(f"Time elapsed: {elapsed_time:.2f} seconds", end="\r")
        time.sleep(0.1)  # Update display every 0.1 seconds
        if elapsed_time >= interval:
            break

interval = 10  # Set the interval in seconds
timer(interval)
