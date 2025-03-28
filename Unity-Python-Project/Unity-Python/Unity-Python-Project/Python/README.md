# Python WebSocket Server

This project includes a simple WebSocket server implemented in Python using the `asyncio` and `websockets` libraries. The server allows for real-time communication with a Unity client.

## Requirements

- Python 3.7 or higher
- `websockets` library

## Installation

To install the required library, run the following command:

```
pip install websockets
```

## Running the Server

1. Navigate to the `Python` directory where `WebsocketServer.py` is located.
2. Run the server using the command:

```
python WebsocketServer.py
```

3. The server will start and listen for connections on `ws://localhost:8765`. You will be prompted to enter messages to send to connected clients.

## Usage

- Connect your Unity client to the WebSocket server.
- Enter messages in the terminal where the server is running to send them to the Unity client.
- The Unity client will log the received messages using `Debug.Log`.