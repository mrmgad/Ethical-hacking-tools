import socket

"""s = socket.socket()
s.connect(("google.com", 80))

import threading

def task():
    print("Running")

t = threading.Thread(target=task)
t.start()"""
import socket
import threading
from queue import Queue

# Target configuration
target = input("Enter target IP or domain: ")
start_port = int(input("Start port: "))
end_port = int(input("End port: "))

# Resolve domain to IP
try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Invalid target.")
    exit()

print(f"\nScanning target: {target_ip}")
print("-" * 40)

# Queue for ports
port_queue = Queue()

# Lock for clean output
print_lock = threading.Lock()

# Worker function
def scan_port():
    while not port_queue.empty():
        port = port_queue.get()
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)

            result = sock.connect_ex((target_ip, port))

            if result == 0:
                with print_lock:
                    print(f"[OPEN] Port {port}")

            sock.close()
        except:
            pass
        finally:
            port_queue.task_done()

# Fill the queue
for port in range(start_port, end_port + 1):
    port_queue.put(port)

# Number of threads
thread_count = 100

threads = []

# Create threads
for _ in range(thread_count):
    t = threading.Thread(target=scan_port)
    t.start()
    threads.append(t)

# Wait for completion
port_queue.join()

print("\nScan completed.")
