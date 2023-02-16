import asyncio

import websockets


# websocket 接受和发送数据
async def handler(websocket):
    while True:
        message = await websocket.recv()
        await websocket.send('消息收到啦,%s' % message)


# websocket监听
async def main():
    async with websockets.serve(handler, "0.0.0.0", 8080):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
