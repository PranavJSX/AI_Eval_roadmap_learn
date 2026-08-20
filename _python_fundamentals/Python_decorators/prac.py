from decorators import do_twice
def parent(num):

    print("Executing parent function")

    def inner1():
        print('Executing from inner 1')
        return None

    def inner2():
        print('Executing from inner 2')
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

#using pie syntax to use decorator
@do_twice
def say_whee():
    print("WHEEE!!")

@do_twice
def call_by_name(name):
    print(f"Hello {name}")



# say_whee = decorator1(say_whee)
def main():
    # parent()

    # first = parent(1)
    # second  = parent(2)

    # print(first())
    # print(second())=

    say_whee()
    call_by_name('Pranav')

if __name__=="__main__":
    main()