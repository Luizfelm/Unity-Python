# This file provides documentation for the Unity client, including setup instructions and how to use the WebSocketClient script.

## Unity WebSocket Client

This Unity script connects to a WebSocket server implemented in Python. It listens for messages from the server and logs them using `Debug.Log`.

### Setup Instructions

1. **Install NativeWebSocket Package**: Ensure you have the NativeWebSocket package installed in your Unity project. You can do this via the Unity Package Manager or by downloading it from the GitHub repository.

2. **Add WebSocketClient Script**: Place the `WebSocketClient.cs` script in the `Assets/Scripts` directory of your Unity project.

3. **Connect to WebSocket Server**: The script is set to connect to a WebSocket server running on `ws://localhost:8765`. Make sure your Python WebSocket server is running before starting the Unity application.

### Usage

- When the Unity application starts, it will connect to the WebSocket server.
- Any messages sent from the Python server will be logged in the Unity console.

### Example

To test the connection, run the Python WebSocket server and then start the Unity application. You can send messages from the server, and they will appear in the Unity console.