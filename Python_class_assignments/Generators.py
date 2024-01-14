'''
Case - Creating fibbonaci sequence.
There are two ways to generate this sequence
1) Lists - More space issues but allows access to all the numbers in sequence via list.
2) Generators - Less space issues but allows access to only current number in sequence at
                a given time.
'''

# Using Lists

lst = [1, 1]                                    # First two numbers in sequence

def fib(n):                                     # Argument needs to be >= 3 for loop to work

    if n < 3 or type(n) != int:
        raise Exception("Please enter a number greater than or equal to 3")

    for i in range(2, n):
        last = lst[i - 1]
        second_last = lst[i - 2]
        current_num = last + second_last
        lst.append(current_num)
    print(lst)

fib(3)

# Using Generators

def fibbonaci(n):                                   # Argument needs to be >= 3 for loop to work
    last_num = 1                                    # First two numbers in sequence
    second_last_num = 1                             # First two numbers in sequence
    count = 3                                       

    if n < 3 or type(n) != int:
        raise Exception("Please enter a number greater than or equal to 3")
    
    while count <= n:
        current_num = last_num + second_last_num
        yield current_num                           # This returns the current number in sequence
        
        second_last_num = last_num
        last_num = current_num
        count += 1
    
for val in fibbonaci(5):
    print(val)