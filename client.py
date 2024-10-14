#!/usr/bin/env python
import asyncio
import websockets

async def chat():
    async with websockets.connect("ws://localhost:8765") as websocket:
        print("Connected to the server.")

        async def send_messages():
            """Allow client to send messages to the server."""
            while True:
                message = input("You: ")
                await websocket.send(message)

        async def receive_messages():
            """Listen for messages from the server."""
            while True:
                message = await websocket.recv()
                print(f"Response from server: {message}")

        # Run both send and receive functions concurrently
        await asyncio.gather(send_messages(), receive_messages())

asyncio.run(chat())
