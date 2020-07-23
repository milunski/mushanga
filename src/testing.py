from time import sleep
import asyncio

async def process():
    await asyncio.sleep(3)
    print("HELLLOOOOOO")

async def process2():
    await asyncio.sleep(6)
    print("HELLLOOOOOO 22222")