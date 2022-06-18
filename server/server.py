import socket
import time

HOST = "127.0.0.1"
PORT = 1234


def server():
    print(f"[SERVER] Starting server on {HOST}:{PORT}\n")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()

        conn, addr = s.accept()

        with conn:
            print(f"[SERVER] New client connected: {addr}\n")

            train_id = conn.recv(1024)
            print(train_id)

            time.sleep(5)


            conn.send(b'Er is een ongeval. Hulptrein is onderweg')
            conn.close()
