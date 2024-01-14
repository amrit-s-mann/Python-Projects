''' Using JOIN & DELAY method in Threading to run threads in sequence '''

## Printing two run statements using different DELAYs in two different threads
import threading
from time import sleep

def run(content, delay):
    sleep(delay)
    print(content)

thread1 = threading.Thread(target = run, args = ("run 1", 1))       # All parameters go in tuple
thread2 = threading.Thread(target = run, args = ("run 2", 2))       # All parameters go in tuple

thread1.start()
print("\nMain thread running")                    # Main thread activates after delay in thread 1
thread2.start()                                 # Thread 2 runs after printing from main thread
print(threading.active_count())                 # All 3 threads running by this point

# Imp to join all threads at end of program in sequence required. 
# This avoids any issue when any module with threads is imported from a main module.
thread1.join()
thread2.join()                                  
print("Done\n")


## Printing sequence of numbers using different DELAYS in two different threads
def print_values(num_lst, delay):
    for val in num_lst:
        print(val)
        sleep(delay)

thread_1 = threading.Thread(target=print_values, args=([1, 3, 5], 0.2))
thread_2 = threading.Thread(target=print_values, args=([2, 4], 0.3))

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()
