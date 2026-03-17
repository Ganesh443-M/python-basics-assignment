

#Task 1

name=str(input("enter you name:"))
age=int(input("enter age:"))
height=float(input("enter height in meters:"))
is_student=input("Are you a student?(yes/no)")
print(name,age, height,is_student)

## Task 2
print(f"Name:{name} Age:{age} |Height:{height} |Student {is_student}")

#Task3
print("age in month:",age*12)
print("age in days:",age*365)
print("Reminder:",age%7)
print("Power of age:",age**2)