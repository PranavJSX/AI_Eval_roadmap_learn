from decorators import *


def parent(num):

    print("Executing parent function")

    def inner1():
        print("Executing from inner 1")
        return None

    def inner2():
        print("Executing from inner 2")
        return None

    if num == 1:
        return inner1

    else:
        return inner2


def decorator1(func):
    def wrapper():
        print("Something is happening before the function")
        func()
        print("Something is happening after the function")

    return wrapper


# using pie syntax to use decorator
@do_twice
def say_whee():
    print("WHEEE!!")


@do_twice
def call_by_name(name):
    print(f"Hello {name}")


@timing
def waste_time(num_times):
    for _ in range(num_times):
        sum([number**2 for number in range(10_000)])


@debugger
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}"
    else:
        return f"Howdy {name} with age {age}"


@slow_down
def countdown(from_number):
    if from_number < 1:
        print("liftoff")
    else:
        print(from_number)
        countdown(from_number - 1)


# say_whee = decorator1(say_whee)
def main():
    # parent()

    # first = parent(1)
    # second  = parent(2)

    # print(first())
    # print(second())=

    say_whee()
    call_by_name("Pranav")
    waste_time(99)
    make_greeting("Pranav", 26)
    countdown(3)


if __name__ == "__main__":
    main()
