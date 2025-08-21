import socket
import os
from tqdm import tqdm

HOST = '0.0.0.0'
PORT = 65432

BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

s = socket.socket()

s.bind((HOST, PORT))

s.listen(5)
print(f"[*] Server mendengarkan di {HOST}:{PORT}")

try:
    client_socket, address = s.accept()
    print(f"[+] {address} telah terhubung.")

    received = client_socket.recv(BUFFER_SIZE).decode()
    filename, filesize = received.split(SEPARATOR)

    filename = os.path.basename(filename)
    filesize = int(filesize)

    print(f"[+] Menerima file: {filename} ({filesize} bytes)")
    with open(filename, "wb") as f:
        with tqdm(total=filesize, unit="B", unit_scale=True, unit_divisor=1024, desc=f"Menerima {filename}") as progress:
            bytes_received = 0
            while bytes_received < filesize:
                bytes_read = client_socket.recv(BUFFER_SIZE)
                if not bytes_read:
                    break
                f.write(bytes_read)
                progress.update(len(bytes_read))
                bytes_received += len(bytes_read)

    print(f"\n[+] File {filename} berhasil diterima.")

except Exception as e:
    print(f"[-] Terjadi error: {e}")
finally:
    if 'client_socket' in locals():
        client_socket.close()
    s.close()
    print("[*] Server ditutup.")