def some_but_not_all(seq, pred): 
    for i in seq:
        result = pred(i)
        print(result)


some_but_not_all('abcdefg', str.isalpha)
print('-'*30)
some_but_not_all([4, 1], lambda x: x>3)