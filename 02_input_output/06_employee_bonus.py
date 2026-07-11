name = input("Enter name of the Employee: ")
salary = float(input("Enter salary: "))
bonus_pct = float(input('Enter bonus percent: '))
bonus_amt=(salary*bonus_pct)/100
total_salary=salary + bonus_amt

print(f"Employee: {name}")
print(f"Salary: {salary}")
print(f"Bonus: {bonus_amt}")
print(f"Total salary: {total_salary}")