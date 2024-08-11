'''
┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┼───┼───┘
    │ 0 │
    └───┘
'''

def get_pins(observed: str):
    keys = {'0':['0','8'],
            '1':['1','2','4'],
            '2':['1','2','3','5'],
            '3':['2','3','6'],
            '4':['1','4','5','7'],
            '5':['2','4','5','6','8'],
            '6':['3','5','6','9'],
            '7':['4','7','8'],
            '8':['5','7','8','9','0'],
            '9':['6','8','9']}
    

    '''
    for i in range(len(observed)+1): # to where
        for j in range(i):           # in where
            for key in keys[observed[j]]:
    '''

    def create_pin(pin:str, index: int):
        if index == len(observed)-1:
            return [pin+key for key in keys[observed[index]]]
        else:
            pins = []
            for key in keys[observed[index]]:
                pins += create_pin(pin+key, index+1)
            return pins

    return create_pin('', 0)



print(get_pins('10'))



''' Better than me:

from itertools import product

ADJACENTS = ('08', '124', '2135', '326', '4157', '52468', '6359', '748', '85790', '968')

def get_pins(observed):
    return [''.join(p) for p in product(*(ADJACENTS[int(d)] for d in observed))]
    
#----------------------------------------------

adjacents = {
  '1': ['2', '4'],
  '2': ['1', '5', '3'],
  '3': ['2', '6'],
  '4': ['1', '5', '7'],
  '5': ['2', '4', '6', '8'],
  '6': ['3', '5', '9'],
  '7': ['4', '8'],
  '8': ['5', '7', '9', '0'],
  '9': ['6', '8'],
  '0': ['8'],
}

def get_pins(observed):
  if len(observed) == 1:
    return adjacents[observed] + [observed]
  return [a + b for a in adjacents[observed[0]] + [observed[0]] for b in get_pins(observed[1:])]    
    
'''