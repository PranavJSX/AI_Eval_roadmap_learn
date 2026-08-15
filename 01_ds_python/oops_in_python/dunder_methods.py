class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = name

    def __str__(self):
        return f"I am {self.name} and my age is {self.age}"

    def __repr__(self):
        return f"{type(self).__name__} (name = '{self.name}', age = '{self.age}')"

# Operator overloading
class Storage(float):
    def __new__(cls, value, unit):
        instance = super().__new__(cls, value)
        instance.unit = unit
        return instance

    def __add__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError(
                "unsupported operant for +: "
                f"'{type(self).__name__}' and '{type(other).__name__}'"
            )
        if not self.unit == other.unit:
            raise TypeError(
                f"incompatible units: '{self.unit}' and '{other.unit}'"
            )

        return type(self)(super().__add__(other), self.unit)


class Factorial():
    def __init__(self):
        self._cache = {0:1, 1:1}

    def __call__(self, number):
        if number not in self._cache:
            self._cache[number] = number * self(number-1)
            print(self._cache)
        return self._cache[number]

class Stack():

    def __contains__(self, item):
        for current_item in self.items:
            if item == current_item:
                return True
            else:
                return False

    def __getitem__(self, index):
        return self.items[index]

    def __len__(self):
        return len(self.items)

    def __reversed__(self):
        return type(self)(reversed(self.items))

def main():
    jane = Person('Jane willie', 25)
    # str(jane)
    # print(jane)
    # print(str(jane))
    # print(repr(jane))

    # Creating objects for storage class
    disk_1 = Storage(500, 'GB')
    disk_2 = Storage(1000, 'GB')
    disk_3 = Storage(1, 'TB')

    # print(disk_1+disk_2)

    # print(disk_2+disk_3)

    factorial_of = Factorial()
    res = factorial_of(5)
    print(res)

if __name__== "__main__":
    main()


