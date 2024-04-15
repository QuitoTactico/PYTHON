import array

filters = array.array('L', [
 0x5555555555555555,
 0x3333333333333333,
 0x0f0f0f0f0f0f0f0f,
 0x00ff00ff00ff00ff,
 0x0000ffff0000ffff,
 0x00000000ffffffff,
 ])

def countBits(n):
    count = 0
    while True:
        n, n64 = n >> 64, n & 0xFFFFFFFFFFFFFFFF
        for ii, f in enumerate(filters):
            a,b = f & n64, ~f & n64
            n64 = a + (b >> (1<<ii))
        count += n64
        if not n: return count