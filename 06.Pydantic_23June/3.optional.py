from pydantic import BaseModel
from typing import Optional

class Employee(BaseModel):
    name:str
    employee_id:Optional[int]=100
    salary:int
    company_name:str="TCS"

new_employee=Employee(name="akshay",salary=100000)

print(new_employee)