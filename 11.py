# -*- coding: UTF-8 -*-
"""
@Project : python_asyncio 
@File    : 11.py
@Author  : lixianbo
@Date    : 2024/8/18 14:30 
"""
# SlingAcademy.com
# This code uses Python 3.11.4
import nest_asyncio
import asyncio

# 允许嵌套事件循环
nest_asyncio.apply()

# 1，定义异步函数
async def hello():
    print("Hello buddy!")
    await asyncio.sleep(1)
    print("Welcome to Sling Academy!")

# 2，创建事件循环
# loop = asyncio.new_event_loop()
loop = asyncio.get_event_loop()
# 3，绑定事件循环
asyncio.set_event_loop(loop)
# 4，运行事件循环
loop.run_until_complete(hello())
# loop.close()