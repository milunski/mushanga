"""


"""

from fastapi import FastAPI
import asyncio
import testing
import threading

app = FastAPI()

@app.get('/')
async def root():
    x = threading.Thread(
        target=asyncio.gather(testing.process(), testing.process2()))
    return {'message': 'Hello World'}