from pydantic import BaseModel

class Employee(BaseModel):
    name: str
    employee_id: int
    salary: int
    company_name: str = "TCS"

new_employee = Employee(name= "akshay", employee_id= 100, salary= 100000)

print(new_employee)