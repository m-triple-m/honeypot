import socket
import datetime

HOST = "0.0.0.0"
PORT = 2222

def log_event(data):
    with open("honeypot_logs.txt", "a") as f:
        f.write(data + "\n")

def start_honeypot():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)

    print(f"[+] Honeypot listening on {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        ip, port = addr

        message = f"[{datetime.datetime.now()}] Connection from {ip}:{port}"
        print(message)
        log_event(message)

        conn.send(b"Fake SSH Server\r\nUsername: ")
        data = conn.recv(1024)

        log_event(f"User attempt from {ip}: {data.decode(errors='ignore')}")
        conn.close()

if __name__ == "__main__":
    start_honeypot()