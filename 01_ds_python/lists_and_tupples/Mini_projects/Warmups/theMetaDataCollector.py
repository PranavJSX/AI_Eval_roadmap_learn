"""
2. Metadata Collector (* Extended Unpacking)
Goal: Practice using the starred * expression to split data.

Scenario: You have user registration data stored in a list:

Python
user_data = ["Alex", "Dev", "Python", "SQL", "Git", "Docker", "USA"]
Requirements:

Unpack user_data into three variables: name (first element), skills (a list of all middle elements), and location (last element).

Print name, skills, and location to confirm it unpacked correctly."""


def main():
    user_data = ["Alex", "Dev", "Python", "SQL", "Git", "Docker", "USA"]
    name, *skills, location = user_data
    print(f"name: {name}, Skills: {skills}, Location: {location}")  

main()
