number_of_employees = int(input("How many employees do you want to add? : "))
employees = []
for emp in range(1, number_of_employees+1):
    employees.append(input(f"Enter Employee {emp}: "))
print(employees)

print('='*40)
print("EMPLOYEE LIST")
print('='*40)

for index in range(len(employees)):
    print(index+1,".",employees[index])