import socket
import os
from tqdm import tqdm

SERVER_HOST = "192.168.137.237"
SERVER_PORT = 65432

BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

filename = input("Masukkan nama file yang ingin dikirim: ")

if not os.path.exists(filename):
    print(f"Error: File '{filename}' tidak ditemukan.")
else:
    filesize = os.path.getsize(filename)

    s = socket.socket()

    try:
        print(f"[+] Menghubungkan ke {SERVER_HOST}:{SERVER_PORT}")
        s.connect((SERVER_HOST, SERVER_PORT))
        print("[+] Terhubung.")

        s.send(f"{filename}{SEPARATOR}{filesize}".encode())

        print(f"[+] Mengirim file: {filename}")
        with open(filename, "rb") as f:
            with tqdm(total=filesize, unit="B", unit_scale=True, unit_divisor=1024, desc=f"Mengirim {filename}") as progress:
                while True:
                    bytes_read = f.read(BUFFER_SIZE)
                    if not bytes_read:
                        break
                    s.sendall(bytes_read)
                    progress.update(len(bytes_read))

        print(f"\n[+] File {filename} berhasil dikirim.")

    except ConnectionRefusedError:
        print(f"[-] Gagal terhubung ke server. Pastikan server sudah berjalan dan IP/Port sudah benar.")
    except Exception as e:
        print(f"[-] Terjadi error: {e}")
    finally:
        s.close()