import socket

target_server = "www.google.com"
target_port = 80

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.settimeout(10)  # don't hang forever

try:
    client_socket.connect((target_server, target_port))

    # Proper HTTP request as BYTES
    request = "GET / HTTP/1.1\r\nHost: google.com\r\nConnection: close\r\n\r\n"
    client_socket.send(request.encode('utf-8'))

    # Receive all data (not just first 4096 bytes)
    response_bytes = b""
    while True:
        chunk = client_socket.recv(4096)
        if not chunk:
            break
        response_bytes += chunk

    # Decode and print nicely
    response_text = response_bytes.decode('utf-8', errors='ignore')
    print(response_text)

except socket.gaierror:
    print("[!] Cannot resolve hostname (DNS issue)")
except ConnectionRefusedError:
    print("[!] Connection refused")
except socket.timeout:
    print("[!] Connection timed out")
except Exception as e:
    print(f"[!] Error: {e}")
finally:
    client_socket.close()