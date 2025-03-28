# Unity-Python Project

This project demonstrates a simple communication setup between a Python WebSocket server and a Unity client. The Python server sends messages to the Unity client, which logs the received messages using `Debug.Log`.

## Project Structure

```
Unity-Python-Project
├── Python
│   ├── WebsocketServer.py       # Python WebSocket server implementation
│   └── README.md                # Documentation for the Python server
├── Unity-Python
│   ├── Assets
│   │   ├── Scripts
│   │   │   ├── WebSocketClient.cs # Unity script for WebSocket client
│   │   │   └── README.md          # Documentation for the Unity client
│   │   └── README.md              # General documentation for Unity assets
└── README.md                      # Main documentation for the project
```

## Getting Started

### Python WebSocket Server

1. **Dependencies**: Ensure you have Python 3.x installed along with the `websockets` library. You can install it using pip:
   ```
   pip install websockets
   ```

2. **Running the Server**: Navigate to the `Python` directory and run the server:
   ```
   python WebsocketServer.py
   ```

3. **Sending Messages**: The server will prompt you to enter messages, which will be sent to connected Unity clients.

### Unity WebSocket Client

1. **Setup**: Open the Unity project located in the `Unity-Python` directory.

2. **NativeWebSocket Package**: Ensure you have the NativeWebSocket package installed. You can find it in the Unity Asset Store or add it via the Package Manager.

3. **Using the WebSocketClient Script**: Attach the `WebSocketClient` script to a GameObject in your Unity scene to start receiving messages from the Python server.

## Conclusion

This project serves as a basic example of how to set up WebSocket communication between a Python server and a Unity client. You can expand upon this foundation to create more complex interactions as needed.