def new_range(start, stop, step):
    count = start

    while True:
        if count <= stop and step < 0:
            return None
        if count >= stop and step > 0:
            return None
    
        yield count
        count += step

iter = new_range(0, -5, -1)
for i in iter:
    print(i)

iter2 = new_range(0, 5, -1)
for j in iter2:
    print(j)

# Testing sync on test_brach1