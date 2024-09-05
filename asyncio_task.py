# -*- coding: UTF-8 -*-
"""
@Project : asyncio_usages 
@File    : asyncio_task.py
@Author  : lixianbo
@Date    : 2024/4/19 14:45 
"""
import asyncio
import time


async def call_api(name: str, delay: float):
    print(f"{name} - step 1")
    await asyncio.sleep(delay)
    print(f"{name} - step 2")


async def main():
    time_1 = time.perf_counter()
    print("start A coroutine")
    task_1 = asyncio.create_task(call_api("A", 2))

    print("start B coroutine")
    task_2 = asyncio.create_task(call_api("B", 3))

    await task_1
    print("task 1 completed")
    await task_2
    print("task 2 completed")

    time_2 = time.perf_counter()
    print(f"Spent {time_2 - time_1}")


asyncio.run(main())