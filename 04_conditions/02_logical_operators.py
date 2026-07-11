#######################################################
# Input
#######################################################
salary = float(input("Enter Salary of the Employee: "))
experience=int(input("Enter Years of Experience: "))

PLATINUM_SALARY=200000
PLATINUM_EXPERIENCE=10

GOLD_SALARY=100000
GOLD_EXPERIENCE=5
#######################################################
# Logic
#######################################################
if salary > GOLD_SALARY and salary < PLATINUM_SALARY and experience >= GOLD_EXPERIENCE:
    status = "Gold Employee" 
elif salary > PLATINUM_SALARY and experience >= PLATINUM_EXPERIENCE:
    status = "Platinum Employee"
else:
    status = "Regular Employee"
#######################################################
# Report
#######################################################
print(f'Employee is an {status}')