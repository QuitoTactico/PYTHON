class CustomMiauError(ValueError):
    pass

def miau(num):
    if num == 0:
        raise ArithmeticError('message miau0')
    elif num == 1:
        raise ZeroDivisionError('message miau1')
    elif num == 2:
        raise KeyError('message miau2')
    elif num == 3:
        raise CustomMiauError('message miau3, custom!')
    else:
        return "Si dió"
    

num = int(input())

try:
    res = miau(num)
    print(res)
except ArithmeticError as e:
    print(e)
    print("it's a ArithmeticError")
except ZeroDivisionError as e:
    print(e)
    print("it's a ZeroDivisionError")
except CustomMiauError as e:
    print(e)
    print("it's a CustomMiauError")
except Exception as e:
    print(f'unrecogniced error with info. {e}')
except:
    print('unrecogniced error with no info.')
else:
    print('este resto de código se correrá si todo salió bien')
finally:
    print('fin, esto se corre sin importar qué')
