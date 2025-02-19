def sum(x, y):
    result = x + y
    return result

nums = {'x': 3, 'y': 4}
print(sum(**nums))  # increíble!

# *nums  :  x y
# **nums :  their values, with keys as parameter : x=3, y=4

# y pues lo que ya sabías de mandar el desempaquetado

nums2 = [1,2,3,4]
print(*nums2, sep='|') # 1|2|3|4


# ver "parámetros infinitos.py" para recibirlos como **kwargs