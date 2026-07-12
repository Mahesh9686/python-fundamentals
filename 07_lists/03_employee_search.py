number_of_employees=int(input("How many employees to add? "))
employees = []

for index in range(1, number_of_employees+1):
    employees.append(input(f"Enter Employee {index}: "))

search_employee = input('Enter employee name to search: ')
if search_employee in employees:
    print(f"Employee Found at position {employees.index(search_employee)}")
else:
    print("Employee Not Found")