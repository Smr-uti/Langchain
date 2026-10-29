from pydantic import BaseModel
from typing import Optional

class Employee(BaseModel):
    name: str
    employee_id: int
    salary: float
    company_name: str= "TCS"

new_employee = Employee(name = "akshay", employee_id= "50", salary = 100000)

print(new_employee)