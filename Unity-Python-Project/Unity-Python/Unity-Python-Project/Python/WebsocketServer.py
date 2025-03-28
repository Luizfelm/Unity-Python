import asyncio
import websockets

async def send_messages(websocket, path):
    while True:
        message = input("Enter a message to send: ")  # Get user input
        await websocket.send(message)
        print(f"Sent: {message}")

async def main():
    start_server = await websockets.serve(send_messages, "localhost", 8765)
    print("WebSocket server started on ws://localhost:8765")
    await start_server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())