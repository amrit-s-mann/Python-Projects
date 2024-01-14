lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_lst = filter(lambda y: y % 2 == 0,map(lambda x: x**2, lst))
print(list(new_lst))

# Alternatively, to print the list, use below
# for i in new_lst:
#     print(i)