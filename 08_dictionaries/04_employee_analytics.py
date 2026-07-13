employees = []
number_of_employees = int(input("How many employees do you want to add? "))
employees_key = ['id', 'name', 'salary']
employees_values=[]
for emp in range(number_of_employees):
    employees_values=[]
    employees_values.append(int(input('Enter ID of the Employee: ')))
    employees_values.append(input('Enter Name of the Employee: '))
    employees_values.append(float(input('Enter the Salary of the Employee: ')))
    employees.append(dict(zip(employees_key,employees_values)))
    print('-'*40)

TOTAL_EMPLOYEES = len(employees)
ADD_SALARY = 0
HIGHEST_SALARY = 0
LOWEST_SALARY = employees[0]['salary']
COUNT_HIGH_SALARY = 0
for emp in employees:
    ADD_SALARY += emp['salary']
    if emp['salary'] > HIGHEST_SALARY:
        HIGHEST_SALARY = emp['salary']
    if emp['salary'] < LOWEST_SALARY:
        LOWEST_SALARY = emp['salary']
    if emp['salary'] > 100000:
        COUNT_HIGH_SALARY += 1
AVERAGE_SALARY = round(ADD_SALARY/TOTAL_EMPLOYEES,2)

print(f"Total Employees             : {TOTAL_EMPLOYEES}")
print(f"Average Salary              : ₹{AVERAGE_SALARY}")
print(f"Highest Salary              : ₹{HIGHEST_SALARY}")
print(f'Lowest Salary               : ₹{LOWEST_SALARY}')
print(f"Employees earning > ₹100000 : {COUNT_HIGH_SALARY}")
