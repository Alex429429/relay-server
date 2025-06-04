import socket
import threading
import time

clients = []

def handle_client(conn, addr):
    print(f"Client connected: {addr}")
    clients.append(conn)
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            timestamp = time.time()
            print(f"Received from {addr} at {timestamp}")
            for c in clients:
                if c != conn:
                    c.send(data)
    except:
        pass
    print(f"Client disconnected: {addr}")
    clients.remove(conn)
    conn.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', 10000))  # TCP-порт
server.listen(2)
print("Relay server started on port 10000")

while True:
    conn, addr = server.accept()
    threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()
