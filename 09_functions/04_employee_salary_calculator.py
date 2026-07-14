def get_employee_details(employees):
    number_of_employees = int(input("How many employees do you want to add? "))
    for emp in range(1, number_of_employees+1):
        employee = {"name" : input("Enter Name of the Employee: "),
                    "salary" : float(input("Enter Basic Salary: ")),
                    "experience" : int(input("Enter Years of Experience: "))}
        employees.append(employee)
        print("-" * 100)

def calculate_bonus(salary,experience):
    if experience < 5:
        bonus = salary * 0.1
    elif experience >= 5:
        bonus = salary * 0.2
    return bonus

def calculate_hra(salary):
    hra = salary * 0.2
    return hra    

def calculate_total_salary(salary, bonus, hra):
    total_salary = salary + bonus + hra
    return total_salary

def print_header():
    row_format = "{:<15} {:<15} {:<15} {:<10} {:<10} {:>20}"
    print(row_format.format("\nEmployee Name", "Basic Salary", "Experience", "Bonus", "HRA", "Total Salary"))
    print('-' * 100)

def print_employee_report(employee, bonus, hra, total_salary):
    row_format = "{:<15} {:<15} {:<15} {:<10} {:<10} {:>20}"
    print(row_format.format(employee['name'], employee['salary'], employee['experience'], bonus, hra, total_salary))

def employee_salary_addons(employees):
    print_header()
    for employee in employees:
        bonus = calculate_bonus(employee["salary"], employee["experience"])
        hra = calculate_hra(employee["salary"])
        total_salary = calculate_total_salary(employee['salary'], bonus, hra)
        print_employee_report(employee, bonus, hra, total_salary)

def main():
    employees = []
    get_employee_details(employees)
    employee_salary_addons(employees)

main()