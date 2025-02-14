def sum_of_digits(num: int):
    # num will be an integer
    return sum(int(i) for i in str(num))