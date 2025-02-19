import functools

def my_decorator(func):

    # el problema es que el nombre original de la función se pierde
    # y se termina llamando wrapper. pierde documentación

    # con esta wea, ya no se sustituye el nombre de la función original
    @functools.wraps(func)
    def wrapper():
        print(f"Running {func.__name__}...")
        func()
        print("Complete")

    return wrapper


@my_decorator
def do_this():
    print("Doing This")

def do_this2():
    print("Doing This 2")


def my_decorator2(func):
    def wrapper(n=None): # te tocaría definir todos los parámetros uno a uno
        print(f"Running {func.__name__}...")
        func(n)
        if n:
            print(f"n is {n}")
        print("Complete")

    return wrapper

def my_decorator3(func):
    def wrapper(*args, **kwargs): # te tocaría definir todos los parámetros uno a uno
        print(f"Running {func.__name__}...")
        func(*args, **kwargs)
        print(f"Complete, with args:{args}, and kwargs: {kwargs}")

    return wrapper


@my_decorator2
def do_that(n: int):
    print("Doing That")

@my_decorator3
def do_that2(*args, **kwargs):
    print("Doing That 2")


do_this()
my_decorator(do_this2()) # no la obliga a ser usada, no tienen el @
do_that(3)
do_that2(3, 2, x=10, y=90)



# ----------------------------------------------
# decorators can also have parameters themselves!


user = {'username':'jose', 'access_level':'guest'}

def make_secure(access_level):
    def decorator(func):

        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user['access_level'] == access_level:
                return func(*args, **kwargs)
            else:
                return f"no {access_level} permissions for {user['username']}"
        
        return secure_function

    return decorator

# como le pasé parámetro, me retornó el decorador necesario
# y el decorador en sí, me retorna una función que atrapa a la función que estoy llamando, get_admin_password
@make_secure("admin")
def get_admin_password():
    return "admin: 1234"
            
