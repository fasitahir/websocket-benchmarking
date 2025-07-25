import asyncio
import websockets
import json

async def echo(websocket):
    """
    Echo server that responds to incoming JSON messages.
    Maintains the same message structure for fair comparison.
    """
    async for message in websocket:
        try:
            # Try to parse as JSON for structured messages
            data = json.loads(message)
            # Echo back the same message for round-trip timing
            await websocket.send(message)
        except json.JSONDecodeError:
            # Handle plain text messages (fallback)
            await websocket.send(message)

async def main():
    print("🚀 Starting WebSocket echo server...")
    async with websockets.serve(echo, "localhost", 8765):
        print("✅ WebSocket server running on ws://localhost:8765")
        print("Press Ctrl+C to stop the server")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n🛑 Server stopped")
