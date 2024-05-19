# Client-Server Chat Application

This is a simple client-server chat application implemented in Python using sockets and the Tkinter library for the GUI.

## Description

The chat application consists of two main components:
- **Server**: Handles incoming connections from clients and broadcasts messages to all connected clients.
- **Client**: Connects to the server, sends messages, and displays messages received from other clients.

The server runs continuously, listening for incoming connections on a specified host and port. Each client connects to the server and provides a nickname to identify themselves. The client's GUI allows them to enter messages and send them to the server, which then broadcasts the messages to all connected clients.

## Features

- Server component to handle connections and broadcast messages.
- Client component with a graphical user interface (GUI) built using Tkinter.
- Clients can choose a nickname to identify themselves.
- Messages are broadcasted to all connected clients in real-time.
- Graceful handling of errors and disconnections.

## Usage

1. Start the server by running `server.py`.
2. Start one or more clients by running `client.py`.
3. Enter a nickname when prompted by the client GUI.
4. Type messages in the client GUI and press "Send" to send messages to the server and other clients.
5. Messages received from other clients will be displayed in the client GUI.

## Files Included

- `server.py`: Contains the server code.
- `client.py`: Contains the client code.
- `README.md`: This file, providing information about the project.

## Requirements

- Python 3.x
- Tkinter library (usually included with Python installation)

## Known Issues

- No support for sending private messages between clients.
- Limited error handling for unexpected client disconnections.
- Lack of encryption and authentication mechanisms for security.

