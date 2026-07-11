employee_name=input("Enter Name of the Employee: ")
employee_id=input("Enter Employee ID: ")
department=input("Enter Department of the Employee: ")
salary=float(input("Enter Salary of the Employee: "))
experience=int(input("Enter Years of Experience: "))
BONUS_EXPERIENCED=20
BONUS_NEW=10
HRA_PERCENT=20

if experience >= 5:
    bonus = salary * BONUS_EXPERIENCED / 100
else:
    bonus = salary * BONUS_NEW / 100

hra = salary * HRA_PERCENT / 100

total_salary = salary + bonus + hra

print("----------------------------------------")
print("EMPLOYEE REPORT")
print("----------------------------------------")

print(f'Employee ID     : {employee_id}')
print(f'Employee Name   : {employee_name}')
print(f'Department      : {department}')
print(f'Experience      : {experience} Years')
print(f'Basic Salary    : {salary}')
print(f'Bonus           : ₹{bonus:,.2f}')
print(f'HRA             : ₹{hra:,.2f}')
print(f'Total Salary    : ₹{total_salary:,.2f}')

if experience >= 10:
    print("Status          : Senior Employee")
else:
    print("Status          : Regular Employee")

if total_salary > 200000:
    print("Income Category : High Income Employee")
else:
    print("Income Category : Normal Income Employee")
print("----------------------------------------")