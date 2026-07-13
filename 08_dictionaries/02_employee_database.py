employees = [
    {
        "id": 101,
        "name": "Mahesh",
        "salary": 122000
    },
    {
        "id": 102,
        "name": "Sahana",
        "salary": 98000
    },
    {
        "id": 103,
        "name": "Arun",
        "salary": 110000
    }
]

print('-' * 40)
print('EMPLOYEE DATABASE')
print('-' * 40)

for employee in employees:
    if employee['salary'] > 100000:
        print(f'ID     : {employee['id']}')
        print(f'Name   : {employee['name']}')
        print(f'Salary : {employee['salary']}')
        print('-' * 40)