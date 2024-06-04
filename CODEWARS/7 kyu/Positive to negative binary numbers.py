def positive_to_negative(binary):
    for a in range(len(binary)):
        binary[a] = 1 if binary[a] == 0 else 0
    
    for i in reversed(list(range(len(binary)))):
        if binary[i] == 0:
            binary[i] = 1
            break
        else:
            binary[i] = 0

    return binary