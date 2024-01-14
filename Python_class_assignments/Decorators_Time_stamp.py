import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        total_time = end_time - start_time
        print("Total time taken to execute:", total_time)
        return result
    return wrapper

@timer
def loop():
    for _ in range(1000000):
        pass

loop()