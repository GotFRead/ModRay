from mod_ray import Answer2Questions
from tests import main_test


import asyncio
import os


async def handler(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')

    print(f"Received {message!r} from {addr!r}")

    Answer2Questions.Answer2Questions.check_avalible_answer(message)


    print(f"Send: {message!r}")
    writer.write(data)
    await writer.drain()

    print("Close the connection")
    writer.close()


async def main():
    host = os.environ.get('host') if os.environ.get('host') is not None else '127.0.0.1'

    port = os.environ.get('port') if os.environ.get('port') is not None else 4000

    server = await asyncio.start_server(
        handler,
        host,
        port)
    
    print(f'Serving on {server.sockets[0].getsockname()}')

    asyncio.create_task(main_test.main())

    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run(main())
