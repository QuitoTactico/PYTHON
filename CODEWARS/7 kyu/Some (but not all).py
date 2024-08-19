def some_but_not_all(seq, pred): return True in [pred(i) for i in seq] and False in [pred(i) for i in seq]


#some_but_not_all('abcdefg', str.isalpha)
some_but_not_all([4, 1], lambda x: x>3)