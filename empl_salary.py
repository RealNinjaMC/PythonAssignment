employees = {}

while True:
    name = input("Enter employee name (type 'stop' to end): ")
    if name.lower() == "stop":
        break

    salary = float(input("Enter basic salary: "))
    hra = salary * 0.20
    da = salary * 0.10
    total = salary + hra + da

    employees[name] = total

print("\nEmployee Salaries:")
for name, total in employees.items():
    print(name, ":", total)
