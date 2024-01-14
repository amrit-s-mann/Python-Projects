''' Printing the numbers in a particular sequence using concurrency '''

import asyncio

async def append_two_values(lst, value1, value2):
    lst.append(value1)
    await asyncio.sleep(0.5)
    lst.append(value2)

async def main():
    task1 = asyncio.create_task(append_two_values(lst, 1, 4))
    task2 = asyncio.create_task(append_two_values(lst, 3, 6))
    task3 = asyncio.create_task(append_two_values(lst, 2, 5))
    
    await asyncio.gather(task1, task2, task3)

lst = []
asyncio.run(main())
print(lst)
