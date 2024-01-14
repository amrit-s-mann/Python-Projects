class Range:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step
    
    def __iter__(self):
        self.current_value = self.start
        return self
    
    def __next__(self):
        if self.step > 0 and self.current_value >= self.stop:
            raise StopIteration
        elif self.step < 0 and self.current_value <= self.stop:
            raise StopIteration
        
        self.current_value += self.step
        return self.current_value - self.step

        
test = Range(3, 10, 2)
itr = iter(test)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))