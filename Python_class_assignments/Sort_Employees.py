def sort_key(item):
    return item[sort_index]

def employee_add():

    while True:
        employee = []
        
        employee_name = input("Enter employee name: ")
        while employee_name.isdigit():
            employee_name = input("Enter employee name: ")
        
        employee_age = input("Enter employee age: ")
        while not employee_age.isdigit():
            employee_age = input("Enter employee age again: ")

        employee_salary = input("Enter employee salary: ")
        while not employee_salary.isdigit():
            employee_salary = input("Enter employee salary again: ")

        employee.extend([employee_name, int(employee_age), int(employee_salary)])
    
        return employee

employee_count = input("Enter the number of employees: ")
while not employee_count.isdigit():
            employee_count = input("Enter the number of employees again: ")

database = []

for idx in range(int((employee_count))):
    database.append(employee_add())

sort_by = input("Enter the sort key amongst 'name' or 'age' or 'salary': ")
while not (sort_by == "name" or sort_by == "age" or sort_by == "salary"):
    sort_by = input("Enter the sort key again: ")

sort_indices = ["name", "age", "salary"]
sort_index = sort_indices.index(sort_by)

sorted_lst = sorted(database, key=sort_key)
print(sorted_lst)




