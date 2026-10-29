from pydantic import BaseModel,Field
from typing import Optional

class Employee(BaseModel):
    name:str=Field(min_length=3,
                   max_length=25)
    employee_id:int=Field(ge=1,
                          lt=1000,
                          default=5,
                          description="this is the unique employee id")
    salary:float
    company_name:str="TCS"

new_employee=Employee(name="akshay",employee_id=999,salary=100000)

print(new_employee)
