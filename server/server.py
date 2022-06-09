import socket
import threading

HOST = "127.0.0.1"
PORT = 1234

clients = {}

def on_client_connect(conn):
    added = False

    while True:
        if added:
            continue

        train_id = conn.recv(1024)

        if not clients.get(train_id):
            clients[train_id] = []

        clients[train_id].append(conn)
        added = True


def server():
    print(f"[SERVER] Starting server on {HOST}:{PORT}\n")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()

        conn, addr = s.accept()

        with conn:
            print(f"[SERVER] New client connected: {addr}\n")

            thread = threading.Thread(target=on_client_connect(conn))
            thread.start()

            print(clients)
