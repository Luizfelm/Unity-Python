# Unity WebSocket Client

This directory contains the Unity client for the WebSocket server implemented in Python. The client connects to the WebSocket server and listens for messages, logging them to the Unity console.

## Setup Instructions

1. **Install NativeWebSocket Package**: Ensure that you have the NativeWebSocket package installed in your Unity project. You can do this via the Unity Package Manager or by downloading it from the GitHub repository.

2. **Add WebSocketClient Script**: Place the `WebSocketClient.cs` script in the `Assets/Scripts` directory of your Unity project.

3. **Attach the Script**: Attach the `WebSocketClient` script to a GameObject in your Unity scene.

4. **Run the WebSocket Server**: Before running the Unity client, make sure to start the Python WebSocket server by executing `WebsocketServer.py`.

5. **Connect to the Server**: When you run the Unity scene, the client will automatically connect to the WebSocket server running on `ws://localhost:8765`.

## Usage

- The Unity client will log any messages received from the Python WebSocket server to the console using `Debug.Log`.
- You can send messages from the Python server by entering them in the terminal where the server is running.