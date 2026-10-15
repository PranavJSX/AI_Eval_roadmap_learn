import time
from typing import Annotated, Self
from datetime import date 
from uuid import UUID, uuid4
from enum import Enum
from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator, PositiveFloat, validate_call


class Department(Enum):
    HR= "HR"
    SALES = "Sales"
    IT = "IT"
    ENGINEERING = "ENGINEERING"

class Employee(BaseModel):
    employee_id: UUID = Field(default_factory=uuid4, frozen=True)
    name: str = Field(min_length=3, frozen=True)
    email: EmailStr 
    date_of_birth: date = Field(alias="birth_date", repr=False, frozen=True)
    salary : float = Field(alias="compensation", gt=0, repr=False)
    department: Department
    elected_benefits: bool

    @field_validator("date_of_birth")
    @classmethod
    def check_valid_age(cls, date_of_birth: date) -> date:
        today = date.today()
        wether_age_21 = date(today.year - 21, today.month, today.day)

        if date_of_birth > wether_age_21:
            raise ValueError("Employee must be at least 21 years old.")

        return date_of_birth

    @model_validator(mode="after")
    def check_if_benefits(self)->Self:
        department = self.department
        elected_benefits = self.elected_benefits

        if department == Department.IT and elected_benefits:
            raise ValueError("IT employees are contract only hence not eligible for benefits.")

        return self


def main():
    employee = Employee(
        name = "Pranav Ojha",
        email = "ojhapranav1999@gmail.com",
        birth_date = "1999-12-09",
        compensation = 96000,
        department = Department.IT,
        elected_benefits = False
    )

    # fail_employee = Employee(
    #     name = False,
    #     email = "123",
    #     date_of_birth = "1992-11-03",
    #     salary = 10110,
    #     department = "Chemistry",
    #     elected_benefits = "Yes"
    # )   

    # new_employee_dict = {
    #     "name": "Chrims Demus",
    #     "email": "cdectuem@gmail.com",
    #     "date_of_birth": "1992-11-03",
    #     "salary": 123_000,
    #     "department": "Sales",
    #     "elected_benefits": False
    # }



    # We can easily instantiate and employee object using the dictionary using the pydantic .model_validate method
    # We also hhave a method called .model_dump() or .model_dump_json() to conver the object back to dictionary or JSON format respectively.
    # print(Employee.model_validate(new_employee_dict).model_dump_json())
    print(employee.model_dump_json())
    # print(fail_employee)

    print()
    print()
    print(Employee.model_json_schema())


# Condition if we want to send an invoice to a customer after getting their details, but before sending we have to validate wheter all the details are correct or not

@validate_call
def send_invoice(
    client_name: Annotated[str, Field(min_length=1)],
    client_email: EmailStr,
    items_purchased: list[str],
    amount_owed: PositiveFloat,
) -> str:

    email_str = f"""
    Dear {client_name}, \n
    Thank you for choosing xyz inc! You
    owe ${amount_owed:,.2f} for the following items:\n 
    {items_purchased}
    """

    print(f"Sending email to {client_email}...")
    time.sleep(2)

    return email_str

email_str = send_invoice(
    client_name = "Pranav Ojha",
    client_email = "manuojha1@gmail.com",
    items_purchased = ["Laptop", "USB Hub"],
    amount_owed = 2245.5
)

print(email_str)


if __name__ == "__main__":
    main()