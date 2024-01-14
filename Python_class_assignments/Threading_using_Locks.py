''' Using LOCK method in Threading to run threads by activating / releasing locks '''

## Using 1 lock to control sequence of output from two different threads
from threading import Lock, Thread
from time import sleep

def t1(lock):
    print("\nThread 1 is running")
    lock.acquire()
    sleep(1)
    print("Thread 1 done")
    lock.release()

def t2(lock):
    print("Thread 2 is running")
    lock.acquire()
    sleep(1)
    print("Thread 2 done\n")
    lock.release()

lock = Lock()
thread1 = Thread(target=t1, args=(lock, ))
thread2 = Thread(target=t2, args=(lock, ))
# Imp to add a ',' if one arguement to make tuple

thread1.start()
thread2.start()

thread1.join()
thread2.join()


## Using 2 locks to control sequence of output from two different threads

def run(content, start_lock, end_lock, name):
    for val in content:
        start_lock.acquire()
        print(f"{name} is running")       
        print(val)
        end_lock.release()

lock1 = Lock()
lock2 = Lock()
lock2.acquire()

thread_1 = Thread(target = run, args = ([1, 3 ,5], lock1, lock2, "Thread 1"))
thread_2 = Thread(target = run, args = ([2, 4], lock2, lock1, "Thread 2"))

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

# Imp to join all threads at end of program in sequence required. 
# This avoids any issue when any module with threads is imported from a main module.
