'''  Using 'AWAIT' & 'SLEEP' function to streamlinea output from different tasks '''

import asyncio
            
async def print_values(values, delay):          # Putting 'async' before def makes it a co-routine
    for i in values:
        print(i)
        await asyncio.sleep(delay)              # await keyword yields control back to main co-routine
    
async def main():
    task1 = asyncio.create_task(print_values([1, 3, 5], 0.2))       # create_task doesn't mean it will run till the end
    task2 = asyncio.create_task(print_values([2, 4], 0.3))

    await task1                                 # await keyword ensures that task is completed before moving to next line
    await task2                                 # This keyword is required whenever multiple co-routines are run.

asyncio.run(main())                             



'''Using 'GATHER' method to combine all tasks in one line '''

import asyncio

async def print_val(values, delay):             # This co-routine remains the same as before
    for i in values:
        print(i)
        await asyncio.sleep(delay)
        
    return delay

async def main_func():
    task_1 = print_val([1, 3, 5], 0.2)
    task_2 = print_val([2, 4], 0.3)
    output = await asyncio.gather(task_1, task_2)       # The 'gather' keyword begins all the tasks and
                                                        # ensures they are completed before moving ahead 
    print(output)

asyncio.run(main_func())
