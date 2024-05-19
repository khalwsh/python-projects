import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 4010

server.bind((host, port))

server.listen(5)

clients = []

nicknames = []

def broadcast(message):
    """
    Broadcasts a message to all connected clients.

    Parameters:
    message (bytes): The message to be broadcasted.
    """
    for client in clients:
        client.send(message)

def handle(client):
    """
    Handles messages received from a client.

    Parameters:
    client (socket.socket): The client socket object.
    """
    while True:
        try:
            message = client.recv(2048)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(index)
            client.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            break

def receive():
    """
    Listens for incoming connections and handles them.
    """
    while True:
        client, address = server.accept()
        client.send("NickName".encode("utf-8"))
        nickname = client.recv(2048).decode("utf-8")
        nicknames.append(nickname)
        clients.append(client)
        broadcast(f"{nickname} connected to server\n".encode("utf-8"))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()
