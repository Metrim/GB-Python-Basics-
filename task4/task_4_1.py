from sys import argv

script_name, salary, per_hour, bonus = argv

print(f"Salary: Base salary: {salary} \nPer hour salary: {per_hour} \nBonus: {bonus} \n\
The total sum: {int(salary) * int(per_hour) + int(bonus)}")
