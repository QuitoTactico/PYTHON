# deprecated
def delete_zeros(lst):
    while i < len(lst):
        if lst[i] == 0:
            lst.pop(i)
        else:
            i += 1
    return lst

def move_zeros(lst):
    zeros = 0
    final = []
    for i in lst:
        if i == 0:
            zeros += 1
        else:
            final.append(i)

    return final+([0]*zeros)
    

print(move_zeros([1,0,0,2,0,0,3,4,5]))