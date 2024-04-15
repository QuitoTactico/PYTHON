def to_binary(num:int) -> str:
    binario = ""
    while num not in [0,1]:
        binario += str(num % 2)
        num = num // 2
    binario += str(num)

    return binario[::-1]

def count_bits(n):
    return to_binary(n).count("1")

# WTFFFFFFFFFFFFFFFF
count_bits_wtf=int.bit_count

print(count_bits_wtf(7))

sapoperro=str.capitalize

