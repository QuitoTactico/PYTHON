def find_closest_number(numbers, target):
    if not numbers: return None

    res = numbers[0]
    diff = abs(numbers[0]-target)

    for i in numbers:
        if abs(i-target) < diff:
            res = i
            diff = abs(i-target)
    
    return res