def my_decorator(func):
    def wrapper():
        print(f"Running {func.__name__}...")
        func()
        print("Complete")
    return wrapper

@my_decorator
def do_this():
    print("Doing This")


def my_decorator2(func):
    def wrapper(n = None):
        print(f"Running {func.__name__}...")
        func(n)
        if n:
            print(f'n is {n}')
        print("Complete")
    return wrapper

@my_decorator2
def do_that(n:int):
    print("Doing That")

do_this()
do_that(3)
