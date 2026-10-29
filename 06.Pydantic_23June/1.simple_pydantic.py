from pydantic import BaseModel

class Employee(BaseModel):
    name: str
    employee_id: int
    salary: int

user_name= input("Enter your name: ")
user_employee_id= input("Enter your employee_id: ")
user_salary= input("Enter your salary: ")

print(type(user_salary))

new_employee = Employee(name=user_name, employee_id=user_employee_id, salary=user_salary)

print(new_employee)