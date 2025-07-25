import asyncio
import websockets
import json
import os

PORT = int(os.environ.get("PORT", 10000))

async def echo(websocket):
    async for message in websocket:
        try:
            data = json.loads(message)
            await websocket.send(message)
        except json.JSONDecodeError:
            await websocket.send(message)

async def main():
    print(f"🚀 Starting WebSocket echo server on port {PORT}...")
    async with websockets.serve(echo, "0.0.0.0", PORT):
        print(f"✅ WebSocket server running on ws://0.0.0.0:{PORT}")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n🛑 Server stopped")
