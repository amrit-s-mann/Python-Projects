## Using ONE class which is not preferred as we CAN'T create separate iterators with different
## internal states, if required

class Numbers:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
    
    def __iter__(self):
        self.count = 0          # This is reset to 0 everytime a new iteration needs to be done.
        return self             # Important line as it returns the iterator object that will be
                                # used later when iteration is invoked using "__next__" dunder.

    def __next__(self):
        self.count += 1

        if self.count == 1:
            return self.num1
        elif self.count == 2:
            return self.num2
        elif self.count == 3:
            return self.num3
        else:
            raise StopIteration

nums = Numbers(7, 8, 9)
itr1 = iter(nums)
itr2 = iter(nums)
print (itr1, itr2)              # Shows that both itr1 & itr2 are SAME iteration object
print(next(itr1))
print(next(itr2))               # Shows that both itr1 to itr2 are in same state.
print(next(itr1))

