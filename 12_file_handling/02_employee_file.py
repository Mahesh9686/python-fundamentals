def get_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Enter Valid Integer!")
            continue

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Enter Valid Integer!")

def get_employee_data():
    employees = []
    number_of_employees = int(input("How many employees do you want to add? "))
    for emp in range(1, number_of_employees+1):
        employee = {
            "employee_id" : get_int_input("Enter Employee ID: "),
            "employee_name" : input("Enter Employee Name: "),
            "department" : input("Enter Department: "),
            "salary" : get_float_input("Enter Salary: "),
            "experience" : get_float_input("Enter Experience: ")
        }
        employees.append(employee)
    return employees

def save_employees(file):
    employees = get_employee_data()
    with open(file, 'a') as employee:
        for emp in employees:            
            for value in list(emp.values()):
                employee.write(str(value))
                employee.write(",")
            employee.write("\n")

def main():
    save_employees("employees.txt")    
main()