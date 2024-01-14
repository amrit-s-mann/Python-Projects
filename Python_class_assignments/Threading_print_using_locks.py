import threading

def print_foo(iterations, start_lock, end_lock):
    for i in range(iterations):
        start_lock.acquire()
        print("foo", end="")
        i += 1
        end_lock.release()

def print_bar(iterations, start_lock, end_lock):
    for i in range(iterations):
        start_lock.acquire()
        print("bar", end="")
        i += 1
        end_lock.release()

count = int(input("\nEnter the number of iterations!\n"))
lock_1 = threading.Lock()
lock_2 = threading.Lock()
lock_2.acquire()

thread_1 = threading.Thread(target = print_foo, args = (count, lock_1, lock_2))
thread_2 = threading.Thread(target = print_bar, args = (count, lock_2, lock_1))

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

