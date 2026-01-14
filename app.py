import socket
from datetime import datetime
from db import init_db, insert_log
from analyzer import is_suspicious
from alerts import send_alert
from config import HOST, PORT

LOG_FILE = "logs/honeypot_logs.txt"

def log_file(text):
    with open(LOG_FILE, "a") as f:
        f.write(text + "\n")

def start_honeypot():
    init_db()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(10)

    print(f"[+] Honeypot running on {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        ip, port = addr

        message = f"[{datetime.now()}] Connection from {ip}:{port}"
        print(message)
        log_file(message)

        conn.send(b"Fake SSH Server\r\nUsername: ")
        data = conn.recv(1024).decode(errors="ignore")

        insert_log(ip, port, data)
        log_file(f"{ip} entered: {data}")

        if is_suspicious(ip):
            print(f"[!] Suspicious repeated activity from {ip}")
            send_alert(ip)

        conn.close()

if __name__ == "__main__":
    start_honeypot()
