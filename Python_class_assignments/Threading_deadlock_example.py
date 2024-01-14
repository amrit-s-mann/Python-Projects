''' Deadlock due to JOIN method on TWO different threads that are calling each other. '''

from threading import Lock, Thread
from time import sleep

def wait_on_threads(threads):
    sleep(1)

    for thread in threads:
        thread.join()

    print("\nThreads have run!")

threads = []                # Added since thread1 cannot use thread2 as it wasn't defined 
thread1 = Thread(target = wait_on_threads, args = (threads, ))
thread2 = Thread(target = wait_on_threads, args = ([thread1], ))
threads.append(thread2)     # After appending thread2, can be used as argument in thread1

thread1.start()
thread2.start()
