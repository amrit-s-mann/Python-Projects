## Using TWO classes which is preferred as we CAN create separate iterators with DIFFERENT
## internal states, if required

# This class creates an iterator using "__iter__" dunder.
class Numbers:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
    
    def __iter__(self):
        return NumIterator(self.num1, self.num2, self.num3)

# This class iterates the iterator using "__next__" dunder.

class NumIterator:
    def __init__(self, one, two, three):
        self.one = one
        self.two = two
        self.three = three
        self.count = 0
    
    def __next__(self):
        self.count += 1
        if self.count == 1:
            return self.one
        elif self.count == 2:
            return self.two
        elif self.count == 3:
            return self.three
        else:
            raise StopIteration

nums = Numbers(4, 5, 6)
itr1 = iter(nums)                #  This is an iterator object created using "__iter__" dunder
print(next(itr1))                #  The iterator is iterated using the "__next__" dunder
print(next(itr1))
print(next(itr1))

itr2 = iter(nums)
print(itr1, itr2)               # Shows that both itr1 & itr2 are DIFFERENT iteration object

print(next(itr2))               # Shows that both itr1 to itr2 are in DIFFERENT state
print(next(itr2))               # that are running independently