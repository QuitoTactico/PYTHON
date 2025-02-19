def multiply(*args):
    if not args: return None

    total = 1
    for n in args:
        total = total * n
    
    return total

print(multiply(1,3,5,10)) # 150


def operate(*args, operator):
    if operator == "+":
        return sum(args)
    elif operator == "*":
        return multiply(args)
    else:
        return "That operator is not handled"
    
#                        operator es obligatorio, como con los prints y su sep o end
print(operate(1,2,3,4,5, operator='+')) # 15


# ---------------------------------

# recibe como diccionario!
# keyword arguments
def print_nicely(**kwargs):
    print(kwargs) # {'x': 10, 'y': 35, 'z': 4000}

    for key, value in kwargs.items():
        print(f'{key} : {value}')

print_nicely(x = 10, y = 35, z = 4000)


# ---------------------------------

# se pueden ambas cosas, para recibir los sin-keyword con *args, y los con keyword con **kwargs

def print_all(*args, **kwargs):
    print(args)   # recibe como tupla, (12, 13, 14, 20)
    print(kwargs) # {'x': 10, 'y': 35, 'z': 4000}

    for item in args:
        print(item)

    for key, value in kwargs.items():
        print(f'{key} : {value}')

print_all(12, 13, 14, 20, x = 10, y = 35, z = 4000)