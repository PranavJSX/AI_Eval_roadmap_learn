class Employee:
    companyName = "Technologies"

    def __init__(self, name, empId, age):

        # Below are all instance attributes

        self.name = name
        self.empId = empId
        self.age = age


class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

    def __str__(self):
        return f" Dog Name : {self.name} and age is {self.age}"


class GermanShepherd(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.speak = "WOOF !!"


def main():
    obj1 = Employee("Pranav Ojha", 141336, 26)
    print(
        f"Employee Name: {obj1.name}, Employee Id: {obj1.empId}, Employee age: {obj1.age}"
    )
    print(Employee.companyName)

    dogMolly = Dog("Molly", 6)
    print(dogMolly)

    germanShepherd1 = GermanShepherd("Bruno", 11)
    print(germanShepherd1)
    print(germanShepherd1.speak)


if __name__ == "__main__":
    main()
