#!/usr/bin/env python
import asyncio
import websockets

# Set to store all connected clients
connected_clients = set()

async def broadcast_message(message, sender):
    """Send the message to all clients except the sender."""
    for websocket in connected_clients:
        if websocket != sender:
            await websocket.send(f"Server Broadcast: {message}")

async def handle_client(websocket):
    """Handle a single connected client."""
    # Add client to the set
    connected_clients.add(websocket)
    try:
        while True:
            # Wait for the client to send a message
            message = await websocket.recv()
            print(f"Received from client: {message}")
            # Broadcast received message to all clients
            await broadcast_message(message, websocket)
            # Optionally, respond directly to the sender
            await websocket.send(f"Server Echo: {message}")
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")
    finally:
        # Remove client from the set when disconnected
        connected_clients.remove(websocket)

async def main():
    async with websockets.serve(handle_client, "localhost", 8765):
        await asyncio.Future()  # Keep the server running

asyncio.run(main())
