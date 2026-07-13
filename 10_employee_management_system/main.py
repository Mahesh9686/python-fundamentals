def menu():
    print("\n")
    print("=" * 100)
    print("EMPLOYEE MANAGEMENT SYSTEM")
    print("=" * 100)
    print("1. Add Employee")
    print("2. Show Employees")
    print("3. Search Employee")
    print("4. Employee Analytics")
    print("5. Update Salary")
    print("6. Delete Employee")
    print("7. Exit")
    selected_option = int(input("\nPlease select an option: "))
    return selected_option

def add_employee(employees):
    number_of_employees = int(input("How many Employees do you want to add? "))
    for emp in range(1, number_of_employees+1):
        employee = {"employee_id" : int(input("Please enter Employee ID: ")),
                    "employee_name" : input("Please enter Employee Name: "),
                    "department" : input("Please enter Employee Department: "),
                    "salary" : float(input("Please enter Employee Salary: ")),
                    "experience" : float(input("Please enter the Employee Experience: "))}
        employees.append(employee)
        print("-" * 100)

def show_employees(employees):
    if len(employees) == 0:
        print("\nNo employees to display.")
        return
    row_format = "{:<12} {:15} {:<30} {:<10} {:>10}"
    print(row_format.format("\nEmployee ID", "Employee Name", "Department", "Salary", "Experience"))
    print('-' * 100)
    for items in employees:
        print(row_format.format(items['employee_id'], items['employee_name'], items['department'], items['salary'], items['experience']))
    

def search_employee(employees):
    if len(employees) == 0:
        print("\nNo employees to search.")
        return
    name = input("Please enter the employee name to search: ")
    row_format = "{:<12} {:15} {:<30} {:<10} {:>10}"
    for items in employees:
        if items['employee_name'] == name:
            print("\nEmployee Found!!")
            print(row_format.format("\nEmployee ID", "Employee Name", "Department", "Salary", "Experience"))
            print('-' * 100)
            print(row_format.format(items['employee_id'], items['employee_name'], items['department'], items['salary'], items['experience']))
            return
    print("\nEmployee Not Found!")

def employee_analytics(employees):
    if len(employees) == 0:
        print("\nNo employees to analyse.")
        return
    row_format = "{:<20} {:<2} {:>4}"
    total_employees = len(employees)
    print(row_format.format('Total Employees', ':', total_employees))
    total_salary = 0
    highest_salary = employees[0]['salary']
    lowest_salary = employees[0]['salary']
    for items in employees:
        total_salary += items['salary']
        if highest_salary < items['salary']:
            highest_salary = items['salary']
        if lowest_salary > items['salary']:
            lowest_salary = items['salary']
    average_salary = total_salary / total_employees
    print(row_format.format('Average Salary', ':', average_salary))
    print(row_format.format('Highest Salary', ':', highest_salary))
    print(row_format.format('Lowest Salary', ':', lowest_salary))

def update_salary(employees):
    if len(employees) == 0:
        print("\nNo employees to display.")
        return
    employee_id = int(input('Enter Employee ID to update salary: '))
    for items in employees:
        if items['employee_id'] == employee_id:
            print(f"Current Salary : {items['salary']}")
            items['salary'] = float(input("Enter New Salary: "))
            print("\nSalary Updated Successfully")
            return
    print("Employee Not Found!")

def delete_employee(employees):
    if len(employees) == 0:
        print("\nNo employees to display.")
        return
    employee_id = int(input('Enter Employee ID to delete: '))
    for index, items in enumerate(employees):
        if items['employee_id'] == employee_id:
            employees.pop(index)
            print('Employee Deleted Successfully')
            return
    print("Employee Not found!")

def exit_program():
    print("Thank you for using Employee Management System!")
    
def main():
    employees = []
    while True:
        selection = menu()
        if selection == 1:
            add_employee(employees)
        elif selection == 2:
            show_employees(employees)
        elif selection == 3:            
            search_employee(employees)
        elif selection == 4:
            employee_analytics(employees)
        elif selection == 5:
            update_salary(employees)
        elif selection == 6:
            delete_employee(employees)
        elif selection == 7:
            exit_program()
            break
        else:
            print("Please select appropriate option")
            
main()
    