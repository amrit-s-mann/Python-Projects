## USING MUTABLE VARIABLE LIKE LIST ##

# OLD METHOD USING CLASS & METHODS

class Collection:
    def __init__(self):
        self.lst = []
    
    def add_value(self, value):
        self.lst.append(value)
        return self.lst

collection = Collection()

for i in range(1, 5):
    collection.add_value(i)
    print(collection.lst)

# NEW METHOD USING CLOSURE FUNCTIONS

def collection():

    lst = []

    def inner(value):
        lst.append(value)
        return lst
    
    return inner

add_value = collection()
for i in range(1, 5):
    print(add_value(i))


## USING IMMUTABLE VARIABLE LIKE INTEGER ##

# OLD METHOD USING CLASS & METHODS

class Counter:

    def __init__(self, start):
        self.count = start
    
    def increment(self, value):
        self.count += value
        return self.count

trial = Counter(2)
print(trial.increment(2))
print(trial.increment(4))
print(trial.increment(6))

# NEW METHOD USING CLOSURE FUNCTIONS

def counter(start):
    count = start

    def increment(value):
        nonlocal count      # <--- Note: Used only in case of immutable variables like int
        count += value
        return count
    
    return increment

test = counter(1)
print(test(2))
print(test(4))
print(test(6))




