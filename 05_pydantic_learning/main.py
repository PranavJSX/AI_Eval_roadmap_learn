from datetime import date 
from uuid import UUID, uuid4
from enum import Enum
from pydantic import BaseModel, EmailStr


class Department(Enum):
    HR= "HR"
    SALES = "Sales"
    IT = "IT"
    ENGINEERING = "ENGINEERING"

class Employee(BaseModel):
    employee_id: UUID = uuid4()
    name: str
    email: EmailStr
    date_of_birth: date
    salary : float
    department: Department
    elected_benefits: bool


def main():
    employee = Employee(
        name = "Pranav Ojha",
        email = "ojhapranav1999@gmail.com",
        date_of_birth = "1999-12-09",
        salary = 96000,
        department = Department.ENGINEERING,
        elected_benefits = True
    )   

    print(employee)

if __name__ == "__main__":
    main()