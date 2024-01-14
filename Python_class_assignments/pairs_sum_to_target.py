def pair_sum(lst1, lst2, target):
    pair_lst = []
    for idx in range(len(lst1)):
        if int(lst1[idx]) + int(lst2[idx]) == int(target):
            pair_lst.append([lst1[idx],lst2[idx]])
        idx += 1
    return pair_lst

def add_elements(count):
    idx = 0
    new_element = 0
    new_lst = []
    for idx in range(int(count)):
        new_element = input("Enter an integer to add in list: ")
        while not new_element.isdigit():
            new_element = input("Enter an integer again: ")
        new_lst.append(new_element)
        idx += 1
    return new_lst

lst_count = input("Enter the number of elements in list: ")
while not lst_count.isdigit():
    lst_count = input("Enter the number of elements again: ")

list1 = add_elements(lst_count)
list2 = add_elements(lst_count)

print(list1, list2)

target = input("Enter a target integer: ")
while not target.isdigit():
    target = input("Enter the target integer again: ")

final_lst = pair_sum(list1, list2, target)
print(final_lst)
