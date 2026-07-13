def calculate_bonus(salary):

    bonus = salary * 0.2

    return bonus

def calculate_hra(salary):

    hra = salary * 0.2

    return hra

def calculate_total(salary,bonus, hra):

    total = bonus + hra + salary

    return total

employee_salary = 122000

employee_bonus = calculate_bonus(employee_salary)
employee_hra = calculate_hra(employee_salary)
total_salary = calculate_total(employee_salary,employee_bonus,employee_hra)
print(f"Salary : {employee_salary}")
print(f"Bonus  : {employee_bonus}")
print(f"HRA    : {employee_hra}")
print(f"Total Salary : {total_salary}")