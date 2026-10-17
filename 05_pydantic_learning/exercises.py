from pydantic import BaseModel, Field, EmailStr, ValidationError

class UserProfile(BaseModel):
    username:str = Field(min_length=3, max_length=20)
    email: EmailStr
    age: float = Field(ge=18)
    is_active: bool = Field(default = True)
    tags: list = Field(default = [])

def main():

    try:
        caseA = UserProfile(
            username = 'Pranav',
            email = 'ojhapranav1999@gmail.com',
            age = 27,
            is_active = True,
            tags = []
        )
        print(caseA)
        print("Case A was succesfully parsed and printed")
    except ValidationError as e:
        print(f"Error {e}")

    try:
        caseB = UserProfile(
            username = 'as',
            email = '',
            age = 19,
            is_active = False,
            tags = []
        )
        print(caseB)
        print("Case B was succesfully parsed and printed")
    except ValidationError as e:
        print(f"Error {e}")
        


if __name__=="__main__":
    main()  