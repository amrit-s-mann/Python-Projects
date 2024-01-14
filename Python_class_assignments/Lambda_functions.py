# Nested lambda functions

result_1 = lambda x: lambda y: x * y
result_2 = result_1(5)
print(result_2(3))

a = lambda y: lambda x: lambda z: print(x + y, end=z)
a("b")("a")("|")

# How it used to work using normal functions

def result_1(x):
    def result_2(y):
        return x + y
    return result_2

output = result_1(2)(7)
print(output)

# Sort-key method using lambda functions

lst = [(10,25), (-13,4), (52,-5),(-92,-12)]
lst.sort(key=lambda x: x[0])
print(lst)

# Positional arguments used in Lambda functions

func = lambda x, y: x + y + 5
z = func(y=11, x=1)
print(z)

# Other examples of using different class types

add_values = lambda x, y, z: print(x + y + z)
max_length = lambda str1, str2: print(max(len(str1),len(str2)))
create_set = lambda lst1, lst2: print(set(lst1).union(set(lst2)))

add_values(22, 44, 55)
max_length("Amritpal","Prerna")
create_set([1,2,4,5],[5,6,7,3])