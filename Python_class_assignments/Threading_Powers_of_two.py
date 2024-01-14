"""
At the end of the program, "powers_of_two" variable needs to contain all of the powers
of 2 within the interval [RANGE_START, RANGE_END).
"""

## Using only JOIN method and no DELAY function

import threading

RANGE_START = 0
RANGE_END = 1000

powers_of_two = set()

def is_power_of_two(x):
    if x == 0:
        return False
    return (x & (x - 1)) == 0

def find_powers_of_two(iter):
    for i in iter:
        if is_power_of_two(i):
            powers_of_two.add(i)

range_1 = range(int(RANGE_START), int(RANGE_END/2))
iter_1 = iter(range_1)

range_2 = range(int(RANGE_END/2 + 1), int(RANGE_END))
iter_2 = iter(range_2)

thread_1 = threading.Thread(target = find_powers_of_two, args = (iter_1, ))
thread_1.start()
thread_1.join()

thread_2 = threading.Thread(target = find_powers_of_two, args = (iter_2, ))
thread_2.start()
thread_2.join()

print(sorted(powers_of_two))

## Using LOCK method and 4 threads

from threading import Thread, Lock

RANGE_START = 0
RANGE_END = 1000

powers_of_two = set()

def is_power_of_two(x):
    if x == 0:
        return False
    return (x & (x - 1)) == 0

def find_powers_of_two(iter):
    for i in iter:
        if is_power_of_two(i):
            thread_lock.acquire()
            powers_of_two.add(i)
            thread_lock.release()

range_1 = range(int(RANGE_START), int(RANGE_END/4))
range_2 = range(int(RANGE_END/4 + 1), int(RANGE_END/2))
range_3 = range(int(RANGE_END/2 + 1), int(RANGE_END*3/4))
range_4 = range(int(RANGE_END*3/4 + 1), int(RANGE_END))

iter_1 = iter(range_1)
iter_2 = iter(range_2)
iter_3 = iter(range_3)
iter_4 = iter(range_4)

thread_lock = Lock()

thread_1 = Thread(target = find_powers_of_two, args = (iter_1, ))
thread_2 = Thread(target = find_powers_of_two, args = (iter_2, ))
thread_3 = Thread(target = find_powers_of_two, args = (iter_3, ))
thread_4 = Thread(target = find_powers_of_two, args = (iter_4, ))

thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()

thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()

print(sorted(powers_of_two))
