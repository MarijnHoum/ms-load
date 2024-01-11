import asyncio
import time
from datetime import datetime

from fastapi import FastAPI

app = FastAPI()

@app.get("/noop")
def get_noop() -> None:
    return None

@app.get("/anoop")
def get_anoop() -> None:
    return None

@app.get("/cpu/{seconds}")
def get_cpu(seconds: float):
    start_time = time.perf_counter()
    end_time = start_time + seconds
    count = 0
    while end_time > time.perf_counter():
        count += 1
    return {
        'seconds': seconds,
        'count': count
    }

@app.get("/acpu/{seconds}")
async def get_acpu(seconds: float):
    return get_cpu(seconds)

@app.get("/wait/{seconds}")
def get_wait(seconds: float):
    time.sleep(seconds)
    return {'seconds': seconds}

@app.get("/await/{seconds}")
async def get_await(seconds: float):
    await asyncio.sleep(seconds)
    return {'seconds': seconds}

@app.get("/mem/{megabytes}/{seconds}")
def get_mem(megabytes: float, seconds: float):
    nr_of_bytes = int(megabytes * 1024 * 1024)
    data = bytearray(nr_of_bytes)  # Allocate the requested bytes.
    time.sleep(seconds)
    del data
    return {
        'megabytes': megabytes,
        'seconds': seconds,
    }
