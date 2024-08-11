
def numbers_of_letters(n):
    str_dict = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
    sol = []
    while True:
        name = ''.join([str_dict[int(i)] for i in str(n)])
        if sol and name == sol[-1]:
            break
        else:
            sol.append(name)
            n = len(name)
    
    return sol

print(numbers_of_letters(60))


''' mucho mejor este:

NUM = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
def numbers_of_letters(n):
    s = ''.join(NUM[i] for i in map(int, str(n)))
    return [s] + (numbers_of_letters(len(s)) if len(s) != n else [])

'''