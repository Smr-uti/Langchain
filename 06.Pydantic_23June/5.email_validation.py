from pydantic import BaseModel, EmailStr
from typing import Optional

class Employee(BaseModel):
    name : str
    employee_id : int
    salary : float
    company_name : str = "TCS"
    email : EmailStr

new_employee=Employee(name="akshay",employee_id="50",salary=100000,email="abc@yahuu.com")

print(new_employee)