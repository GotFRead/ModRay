import asyncio


async def main():
    reader, writer = await asyncio.open_connection('127.0.0.1', 4000)
  
    message = 'Give_me_operator'
    
    print(f'Send: {message!r}')
    writer.write(message.encode())

    print('Close the connection')
    writer.close()

if __name__ == '__main__':
    asyncio.run(main())
