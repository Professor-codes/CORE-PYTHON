employee = {
    "maxim": 10000,
    "john": 52000,
    "zia": 44000,
    "sara": 198000,
    "tor": 2000,
    "jack": 2000,
    "katy": 10,
    "tarry": 700,
    "rosa": 1300,
    "corner": 1800,
}

# print(employee.keys())
# print(employee.values())
# print(employee.items())
# print(employee["maxim"])
# print(employee["corner"])

# for index, emp in enumerate(employee):
#     print(index+1, emp, employee[emp])

name = input("employee name : ")

if name in employee:
    print(f"The salary of {name} is {employee[name]}")
else:
    print(f"{name} not found")
